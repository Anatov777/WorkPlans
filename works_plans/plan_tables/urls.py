from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plan_<plan_id>/<year_id>', views.chooseYear, name='urlYear'),
    path('plan_<plan_id>', views.choosePlanId, name='urlPlanNumber'),
]
