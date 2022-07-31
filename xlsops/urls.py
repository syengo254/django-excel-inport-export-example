from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('import/', views.import_data, name="import"),
    path('export/', views.export_data, name="export"),
]
