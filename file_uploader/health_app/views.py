from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
import datetime


def request_time():
    return datetime.datetime.now()


class HealthView(View):
    def get(self, request):
        return HttpResponse({"status": "ok", "date": request_time()})


class DatabaseHealthView(View):
    def get(self, request):
        date = request_time()
        try:
            User.objects.all()
            return HttpResponse({
                "status": "database is running",
                "date": date
            })
        except Exception:
            return HttpResponse({
                "status": "database is not running",
                "date": date
            })
