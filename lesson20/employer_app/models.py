from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Vacancy(models.Model):
    name_vacancy = models.CharField(max_length=55)
    name_company = models.CharField(max_length=55)
    salary = models.PositiveIntegerField()
    required_skills = models.CharField(max_length=55)
    responsibilities = models.CharField(max_length=55)
    address = models.PositiveIntegerField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return f'{self.name_vacancy} - {self.name_company}'

    def get_absolute_url(self):
        return reverse('vacancy_slug', kwargs={'vacancy_slug': self.slug, 'pk': self.pk})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.name_vacancy}-{self.name_company}')
        super().save(force_insert, force_update, using, update_fields)
        return f'{self.name_vacancy} - {self.name_company}'


