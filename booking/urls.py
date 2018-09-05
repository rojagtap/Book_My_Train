from django.conf.urls import url
from . import views

app_name = 'booking'

urlpatterns = [
    url(r'^$', views.login_user, name='login_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^detail/book/(?P<amt>[0-9]+)/(?P<passengers>[0-9]+)/(?P<is_return>[a-zA-Z]+)$', views.book, name='book'),
    url(r'^status/$', views.status, name='status'),
]
