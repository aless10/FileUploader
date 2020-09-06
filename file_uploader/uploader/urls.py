from django.urls import path

from .views import UploadView, ThanksView, UploadFileList

urlpatterns = [
    path(
        '',
        UploadView.as_view(),
        name='upload-view'
    ),
    path(
        r'thanks',
        ThanksView.as_view(),
        name='thanks-view'
    ),
    path(
        r'list/<uuid:link>',
        UploadFileList.as_view(),
        name='file-list-view'
    )
]
