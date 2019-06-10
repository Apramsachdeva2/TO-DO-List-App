from django.urls import path
from . import views

urlpatterns = [
path('',views.home, name="index"),
path('add',views.add,name='add'),
path('complete/<item_id>',views.complete,name='complete'),
path('deletecompleted',views.deletecomplete,name='deletecomplete'),
path('deleteall',views.deleteall,name='deleteall')
]
