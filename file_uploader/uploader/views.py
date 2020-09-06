from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, ListView

from .forms import FileUploadForm
from .models import Link, File


class UploadFileList(ListView):
    model = File
    template_name = "file_list.html"

    def get_files_by_reference(self, link):
        return self.model.\
            objects.filter(link__slug=link)  # pylint:disable=E1101

    def get(self, request, *args, **kwargs):
        # if password is set => show modal whit password
        # and then redirect to this list
        # if expiry date is set => return expired link and redirect to homepage
        link = str(kwargs.get("link"))
        files = self.get_files_by_reference(link=link)
        return render(request, self.template_name, {'files': files})


class ThanksView(TemplateView):
    template_name = "thanks.html"


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
            return HttpResponseRedirect(self.success_url,
                                        {
                                            "link": link.slug,
                                            "password": link.password,
                                            "expiry_date": link.expiry_date
                                        }
                                        )
        else:
            return render(request, self.template_name, {'form': form})
