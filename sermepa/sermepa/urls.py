from django.conf.urls.defaults import *

urlpatterns = patterns('sermepa.sermepa.views',
    url(
        regex=r'^$',
        view='sermepa_ipn',
        name='sermepa_ipn',
    ),         
)
