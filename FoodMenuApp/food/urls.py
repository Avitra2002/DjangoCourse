from django.urls import path
from . import views

app_name= 'food' ##for django to know which app to look out for when a /index or /detail is called as other apps might have the same router name
urlpatterns = [
    ## for /food/
    path("", views.index, name="index"),
    ## for /food/hello/
    path("hello/", views.index,name='index'),
    path("item/", views.item, name='item'),
    ## for /food/1
    path('<int:item_id>/',views.detail,name='detail'), ##path that expects an int that is called item_id that will be passed to the detail controller as input


]