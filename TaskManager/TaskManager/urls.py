"""
URL configuration for Todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    path("list/<int:list_id>/item/add/", views.ItemCreate.as_view(), name="item-add",),
    path("list/<int:list_id>/item/<int:pk>/", views.ItemUpdate.as_view(),name="item-update",),
    path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    path("list/<int:list_id>/item/<int:pk>/delete/", views.ItemDelete.as_view(), name="item-delete",),
]