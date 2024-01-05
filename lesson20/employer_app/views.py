from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from applicant_app.models import Resume
from employer_app.forms import VacancyForm
from employer_app.models import Vacancy


def resume_list_view(request):
    context = {'resume_list': Resume.objects.all()}

    return render(request, 'employer_app/resume_list.html', context)


def resume_detail_view(request, resume_slug):
    resume = Resume.objects.get(slug=resume_slug)
    context = {'resume_slug': resume}

    return render(request, 'employer_app/resume_detail.html', context)


def vacancy_list_view(request):
    context = {'vacancy_list': Vacancy.objects.all()}

    return render(request, 'employer_app/vacancy_list.html', context)


def vacancy_detail_view(request, vacancy_slug):
    vacancy = Vacancy.objects.get(slug=vacancy_slug)
    context = {'vacancy_slug': vacancy}

    return render(request, 'employer_app/vacancy_detail.html', context)


def vacancy_create_view(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = VacancyForm()
    context = {'form': form}

    return render(request, 'employer_app/vacancy_create.html', context)


def vacancy_delete_view(request):
    if request.method == 'POST':
        name_company = request.POST.get('name_company')

        Vacancy.objects.filter(name_company=name_company).delete()

        return redirect('resume_list')

    return render(request, 'employer_app/vacancy_delete.html')


# class VacancyUpdate(UpdateView):
#     template_name = 'employer_app/vacancy_update.html'
#     model = Vacancy
#     form_class = VacancyForm
#     success_url = reverse_lazy('resume_list')


def vacancy_update_view(request, pk):
    vacancy = Vacancy.objects.get(pk=pk) if Vacancy.objects.filter(pk=pk).exists() else None
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = VacancyForm(instance=vacancy)

    context = {'form': form}

    return render(request, 'employer_app/vacancy_update.html', context)



