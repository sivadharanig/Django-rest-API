from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *
# method One
urlpatterns=[
    path('allCatageryOthers/',catageryview.as_view()),
    path('allCatageryOthers/<uuid:pk>/',catageryview.as_view()),
    path('allCatagery/<uuid:pk>/',catageryview.as_view()),
    path('allCatageryOthersV2/<uuid:pk>/',catageryviewversion.as_view()),
    # path('Name/', CustomeCatagery.as_view())
]

