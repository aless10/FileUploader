from django.urls import path

from .views import HealthView, DatabaseHealthView

urlpatterns = [
    path(
        r'app-health',
        HealthView.as_view(),
        name='health-view'
    ),
    path(
        r'database-health',
        DatabaseHealthView.as_view(),
        name='database-health-view'
    ),
]
