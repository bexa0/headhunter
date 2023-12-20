from django.shortcuts import render, redirect, get_object_or_404
from applicant_app.models import Resume
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


def vacancy_detail_view(request, vacancy_slug, resume_slug):
    vacancy = Vacancy.objects.get(slug=vacancy_slug)
    resume_s = get_object_or_404(Resume, slug=resume_slug)
    context = {'vacancy_slug': vacancy, 'resume_slug': resume_s}

    return render(request, 'employer_app/vacancy_detail.html', context)


def vacancy_create_view(request):
    context = {'vacancy_create': Vacancy.objects.all()}

    if request.method == 'POST':
        name_vacancy = request.POST.get('name_vacancy')
        name_company = request.POST.get('name_company')
        salary = request.POST.get('salary')
        required_skills = request.POST.get('required_skills')
        responsibilities = request.POST.get('responsibilities')
        address = request.POST.get('address')

        vacancy = Vacancy()

        vacancy.name_vacancy = name_vacancy
        vacancy.name_company = name_company
        vacancy.salary = salary
        vacancy.required_skills = required_skills
        vacancy.responsibilities = responsibilities
        vacancy.address = address
        vacancy.save()

        return redirect('main')

    return render(request, 'employer_app/vacancy_create.html', context)


def vacancy_delete_view(request):
    context = {'vacancy': Vacancy.objects.all()}
    if request.method == 'POST':
        name_vacancy = request.POST.get('name_vacancy')

        Vacancy.objects.filter(name_vacancy=name_vacancy).delete()

        return redirect('resume_list')

    return render(request, 'employer_app/vacancy_delete.html', context)



