from django.urls import path
from .views import home, policy, calculator, download_pdf


urlpatterns = [
    path('', home, name='home'),
    path('policy/', policy, name='policy'),
    path('calculator/', calculator, name='calculator'),
    path('download_pdf/<path:pdf_path>/', download_pdf, name='download_pdf'),
]
