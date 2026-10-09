from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_view, name='root'),
    path('analyze', views.analyze_pdf, name='analyze'),
    path('api/upload', views.upload_resume, name='upload'),
    path('api/suggestions', views.get_suggestions, name='suggestions'),
    path('api/auth/register', views.register, name='register'),
    path('api/auth/login', views.login_view, name='login'),
]
