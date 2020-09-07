from django.contrib.messages import get_messages
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.shortcuts import render, get_list_or_404
from django.views.generic import FormView, TemplateView, ListView
from django.contrib import messages

from .forms import FileUploadForm, UnlockForm
from .models import Link, File
from .utils import is_the_past


class UploadFileList(ListView):
    model = File
    template_name = "file_list.html"
    form_class = UnlockForm

    def get_files_by_reference(self, link):
        return self.model. \
            objects.filter(link__slug=link)  # pylint:disable=E1101

    def return_file_list(self, request, link_obj):
        files = get_list_or_404(self.model, link=link_obj)
        return render(
            request,
            self.template_name,
            {'files': files, 'link': str(link_obj.slug)}
        )

    def get(self, request, *args, **kwargs):
        link = str(kwargs.get("link"))
        link_obj = Link.objects.get(slug=link)  # pylint:disable=E1101
        if request.GET.get("password") is None:
            expiry_date = link_obj.expiry_date
            if link_obj is None:
                raise Http404(
                    f"The link {link} that you provided does not exists"
                )
            elif link_obj.password is not None:
                form = self.form_class()
                return render(
                    request,
                    self.template_name,
                    {'password': True, "form": form}
                )
            elif expiry_date is not None and is_the_past(expiry_date):
                messages.add_message(request, messages.WARNING, {
                    "link": link_obj.slug,
                    "expiry_date": expiry_date
                })
                return HttpResponseRedirect("/")
            else:
                return self.return_file_list(request, link_obj)
        else:
            password = request.GET.get("password")
            if password != link_obj.password:
                return HttpResponseForbidden(
                    f"Invalid password for link {link}"
                )
            else:
                return self.return_file_list(request, link_obj)


class ThanksView(TemplateView):
    template_name = "thanks.html"

    def get(self, request, *args, **kwargs):
        storage = get_messages(request)
        data = {}
        for message in storage:
            data.update({"link": message.message})
        return render(request, self.template_name, {"data": data})


class UploadView(FormView):
    template_name = 'upload.html'
    form_class = FileUploadForm
    success_url = 'thanks'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')
        if form.is_valid():
            link = Link(
                password=form.cleaned_data.get("password"),
                expiry_date=form.cleaned_data.get("expiry_date"),
            )
            link.save()
            for f in files:
                file_obj = File(
                    file=f,
                    filename=f.name,
                    link=link
                )
                file_obj.save()

            messages.add_message(request, messages.SUCCESS, str(link.slug))
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request, self.template_name, {'form': form})
