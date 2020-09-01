from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index),
    path('AddRam.html/', views.AddRam),
    path('Add.html/', include('Spec.urls')),
    path('Options.html/', views.OptionsAct),
    path('Trip.html/', views.Trip),
    path('Order.html/', views.Order),
]

urlpatterns += staticfiles_urlpatterns()