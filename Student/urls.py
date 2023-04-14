from django.urls import path

from Student import views

urlpatterns = [
    path('',views.home),
    path('displaystudent',views.displaystudent,name='displaystudent'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('readstudentdata',views.readstudentdata,name='readstudentdata'),
    path('update/<int:id>',views.updatestudent,name='update'),
    path('delete/<int:id>',views.deletestudent,name='delete'),
]