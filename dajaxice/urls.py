from .views import DajaxiceRequest
from django.conf.urls import url

urlpatterns = [
    url(r'^(.+)/$', DajaxiceRequest.as_view(), name='dajaxice-call-endpoint'),
    url(r'', DajaxiceRequest.as_view(), name='dajaxice-endpoint'),
]
