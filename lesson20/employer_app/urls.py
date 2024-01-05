from django.urls import path
from .views import *

urlpatterns = [
    path('resume-list/', resume_list_view, name='resume_list'),
    path('resume-list/detail/<slug:resume_slug>/', resume_detail_view, name='resume_detail'),
    path('vacancy-list/', vacancy_list_view, name='vacancy_list_staff'),
    path('vacancy-list/detail/<slug:vacancy_slug>/<slug:resume_slug>/', vacancy_detail_view, name='vacancy_detail_staff'),
    path('vacancy-create/', vacancy_create_view, name='vacancy_create'),
    path('vacancy-delete/', vacancy_delete_view, name='vacancy_delete'),
    path('vacancy-update/<int:pk>/', vacancy_update_view, name='vacancy_update'),
]