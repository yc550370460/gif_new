from django.conf.urls import include, url
from django.contrib import admin
from gif_app.views import index, gif

urlpatterns = [
    # Examples:
    # url(r'^$', 'gif.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    url(r'^gif/', gif),
]
