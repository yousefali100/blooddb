from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from api.views import *


urlpatterns = [

	re_path("stock/((?P<pk>\d+)/)?", csrf_exempt(StockView.as_view())),
	re_path("bloodrequest/((?P<pk>\d+)/)?", csrf_exempt(BloodRequestView.as_view())),
	re_path("patient/((?P<pk>\d+)/)?", csrf_exempt(PatientView.as_view())),
	re_path("donor/((?P<pk>\d+)/)?", csrf_exempt(DonorView.as_view())),
	re_path("blooddonate/((?P<pk>\d+)/)?", csrf_exempt(BloodDonateView.as_view())),

]