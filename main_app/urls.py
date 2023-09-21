from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:pk>', views.FinchesDetail.as_view(), name='finch_detail'),
    path('finches/new', views.FinchesCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/edit', views.FinchesUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete', views.FinchesDelete.as_view(), name='finch_delete'),
    
]