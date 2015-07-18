from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'staypay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'hotel.views.mainPage'),
    url(r'^/(?P<hotel_id>[0-9]+)/$', 'hotel.views.hotelId'),
)
