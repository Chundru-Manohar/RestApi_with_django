from .import views
from django.urls import path

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add/',views.Student_adds,name='add'),
    path('update/<int:id>/',views.Student_update,name='update'),
    path('delete/<int:id>/',views.Student_delete,name='update'),
   
]
