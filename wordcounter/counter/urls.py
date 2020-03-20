from . import views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('frequency/',views.index,name='index'),
    path('results/<str:pk>/',views.result,name='result'),
    path('', RedirectView.as_view(url='frequency')),
]
