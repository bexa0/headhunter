from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from applicant_app.forms import ResumeForm
from applicant_app.models import Resume
from employer_app.forms import VacancyForm
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


def vacancy_detail_view(request, vacancy_slug):
    vacancy = Vacancy.objects.get(slug=vacancy_slug)
    context = {'vacancy_slug': vacancy}

    return render(request, 'applicant_app/vacancy_detail.html', context)


def resume_create_view(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = ResumeForm()
    context = {'form': form}

    return render(request, 'applicant_app/resume_create.html', context)


def resume_delete_view(request):
    context = {'resume':  Resume.objects.all()}
    if request.method == 'POST':
        name = request.POST.get('name')

        Resume.objects.filter(name=name).delete()

        return redirect('vacancy_list')

    return render(request, 'applicant_app/resume_delete.html', context)


def resume_update_view(request, pk):
    resume = Resume.objects.get(pk=pk) if Resume.objects.filter(pk=pk).exists() else None
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = ResumeForm(instance=resume)

    context = {'form': form}

    return render(request, 'applicant_app/resume_update.html', context)