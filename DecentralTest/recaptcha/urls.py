from django.urls import path
from . import views

urlpatterns = [
    path('', views.fnGenerateCaptcha, name='generate_captcha'),
    path('app', views.fnGenerateCaptcha, name='generate_captcha'),
    path('code', views.fncheckcode, name='checkcode')
]
