from django.conf.urls import url
from . import views

# fce vraci seznam prispevku na hlavni strance:
urlpatterns = [url('^$', views.post_list, name='post_list')]    # ^ je zacatek a $ konec retezce
