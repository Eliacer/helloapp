from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^home/$', views.home.as_view()),
    url(r'^about/$', views.about.as_view()),
    url(r'^contact/$', views.contact.as_view()),
    url(r'^blog/$', views.contact.as_view()),
]