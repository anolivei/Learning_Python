from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("angelica", views.angelica, name="angelica")
]