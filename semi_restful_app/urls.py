from django.urls import path
from . import views

urlpatterns=[
    path('shows/new', views.index),
    path('shows/create', views.create),
    path('shows/<id>', views.display),
    path('shows', views.shows),
    path('shows/<id>/edit', views.edit),
    path('shows/<id>/update', views.update),
    path('shows/<id>/destroy', views.destroy),
]