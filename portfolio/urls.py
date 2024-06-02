from django.urls import path
from .views import*
from .pdf import resume_pdf

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('pdf/', resume_pdf, name='pdf'),
]
