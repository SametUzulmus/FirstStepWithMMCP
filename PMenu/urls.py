from django.urls import path
from PMenu import views

urlpatterns=[
    path("",views.HomePage,name="HomePage"),
    path("Python/Menu1",views.Pmenu1,name="PMenu1"),
    path("Python/Menu2",views.Pmenu2,name="PMenu2"),
    path("Python/Menu3",views.Pmenu3,name="PMenu3"),
    
]
