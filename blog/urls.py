from django.conf.urls import url
from . import views

# fce vraci seznam prispevku na hlavni strance:
urlpatterns = [url('^$', views.post_list, name='post_list'),    # ^ je zacatek a $ konec retezce
               url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
               url('^post/new$', views.post_new, name='post_new'),
               ]
