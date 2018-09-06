from django.conf.urls import include, url
from django.contrib import admin
from gif_app.views import index, gif, manage

urlpatterns = [
    # Examples:
    # url(r'^$', 'gif.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/', index),
    url(r'^gif/\d+', gif),
    url(r'^manage/', manage),
]
