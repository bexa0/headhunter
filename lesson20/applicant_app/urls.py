from django.urls import path
from .views import *

urlpatterns = [
    path('', StartPageView.as_view(), name='main'),
    path('signup/', SignUpView.as_view(), name='sign_up'),
    path('login/', UserLoginView.as_view(), name='log_in'),
    path('logout/', UserLogoutView.as_view(), name='log_out'),
    path('vacancy-list/', vacancy_list_view, name='vacancy_list'),
    path('vacancy-list/detail/<slug:vacancy_slug>/', vacancy_detail_view, name='vacancy_detail'),
    path('create-resume/', resume_create_view, name='create_resume'),
    path('delete-resume/', resume_delete_view, name='delete_resume'),
    path('update-resume/<int:pk>/', resume_update_view, name='update_resume'),
]