from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plan_tables/', include('plan_tables.urls')),
    path('plan_tables/print_tables/', include('print_tables.urls')),
    path('plan_tables/create_plan/', include('create_plan.urls')),

    path('auth/', include('loginsys.urls')),
    path('', include('loginsys.urls')),
]
