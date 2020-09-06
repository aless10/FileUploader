from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
import datetime


def request_time():
    return datetime.datetime.now()


class HealthView(View):
    def get(self, request):
        return JsonResponse({"status": "ok", "date": request_time()})


class DatabaseHealthView(View):
    def get(self, request):
        date = request_time()
        try:
            User.objects.all()
            return JsonResponse({
                "status": "database is running",
                "date": date
            })
        except Exception:
            return JsonResponse({
                "status": "database is not running",
                "date": date
            })
