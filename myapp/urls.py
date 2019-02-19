from django.urls import path
from myapp import views

urlpatterns=[

    path('myModel/',views.myMoldeList.as_view(),name=views.myMoldeList.name),
    path('myModel/<int:pk>',views.myModelDetail.as_view(),name=views.myModelDetail.name)
]