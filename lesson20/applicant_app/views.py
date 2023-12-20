from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from applicant_app.models import Resume
from employer_app.models import Vacancy


class StartPageView(TemplateView):
    template_name = 'applicant_app/start.html'

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)


class SignUpView(CreateView):
    template_name = 'applicant_app/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('main')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')

        return super().get(request, *args, **kwargs)


class UserLoginView(LoginView):
    template_name = 'applicant_app/log_in.html'
    form_class = AuthenticationForm
    next_page = reverse_lazy('main')


class UserLogoutView(LogoutView):
    template_name = 'applicant_app/log_out.html'
    next_page = reverse_lazy('main')


def vacancy_list_view(request):
    context = {'vacancy_list': Vacancy.objects.all()}

    return render(request, 'applicant_app/vacancy_list.html', context)


def vacancy_detail_view(request, vacancy_slug, resume_slug):
    vacancy = Vacancy.objects.get(slug=vacancy_slug)
    resume_s = Resume.objects.get(slug=resume_slug)
    context = {'vacancy_slug': vacancy, 'resume_slug': resume_s}

    return render(request, 'applicant_app/vacancy_detail.html', context)


def resume_create_view(request):
    context = {'resume_create': Resume.objects.all()}

    if request.method == 'POST':
        name_vacancy = request.POST.get('name_vacancy')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        middle_name = request.POST.get('middle_name')
        date_born = request.POST.get('date_born')
        email = request.POST.get('email')
        skills = request.POST.get('skills')
        professional_experience = request.POST.get('professional_experience')
        education = request.POST.get('education')

        resume = Resume()

        resume.name_vacancy = name_vacancy
        resume.name = name
        resume.surname = surname
        resume.middle_name = middle_name
        resume.date_born = date_born
        resume.email = email
        resume.skills = skills
        resume.professional_experience = professional_experience
        resume.education = education
        resume.save()

        return redirect('main')

    return render(request, 'applicant_app/resume_create.html', context)


def resume_delete_view(request):
    context = {'resume':  Resume.objects.all()}
    if request.method == 'POST':
        name = request.POST.get('name')

        Resume.objects.filter(name=name).delete()

        return redirect('vacancy_list')

    return render(request, 'applicant_app/resume_delete.html', context)


class ResumeUpdateView(UpdateView):
    template_name = 'applicant_app/resume_update.html'
    model = Resume
    slug_url_kwarg = 'resume_slug'
    fields = ('name_vacancy', 'name', 'surname', 'middle_name', 'date_born', 'email', 'skills',
              'professional_experience', 'education')
    success_url = reverse_lazy('vacancy_list')


# def resume_update_view(request, resume_slug):
#     resume_s = get_object_or_404(Resume, slug=resume_slug)
#     context = {'resume_slug': resume_s}
#
#     return render(request, 'applicant_app/resume_update.html', context)


# def resume_update_view(request, id):
#     resume = Resume.objects.filter(pk=id)
#     context = {'resume': resume}
#
#     if request.method == 'POST':
#         name_vacancy = request.POST.get('name_vacancy')
#         name = request.POST.get('name')
#         surname = request.POST.get('surname')
#         middle_name = request.POST.get('middle_name')
#         date_born = request.POST.get('date_born')
#         email = request.POST.get('email')
#         skills = request.POST.get('skills')
#         professional_experience = request.POST.get('professional_experience')
#         education = request.POST.get('education')
#
#         resume.name_vacancy = name_vacancy
#         resume.name = name
#         resume.surname = surname
#         resume.middle_name = middle_name
#         resume.date_born = date_born
#         resume.email = email
#         resume.skills = skills
#         resume.professional_experience = professional_experience
#         resume.education = education
#         resume.save()
#
#         return redirect('vacancy_list')
#
#     return render(request, 'applicant_app/resume_update.html', context)
