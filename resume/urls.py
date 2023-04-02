from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.resume_home, name="resume_home"),
    path('resume_form/',views.resume_form, name="resume_form" ),
]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

