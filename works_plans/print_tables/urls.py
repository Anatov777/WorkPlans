from django.urls import path

from . import views

urlpatterns = [
    path('plan_<plan_id>/<year_id>', views.fall_table, name='fall_table'),
]
