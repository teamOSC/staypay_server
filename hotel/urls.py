from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'staypay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'hotel.views.mainPage'),
    url(r'^/(?P<hotel_id>[0-9]+)/$', 'hotel.views.hotelId'),
    url(r'^/(?P<hotel_id>[0-9]+)/room/(?P<room_number>[0-9]+)/$', 'hotel.views.roomFunctions'),
    url(r'^/(?P<hotel_id>[0-9]+)/(?P<room_type>[0-9]+)/$', 'hotel.views.bookRoom'),
)
