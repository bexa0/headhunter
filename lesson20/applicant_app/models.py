from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Resume(models.Model):
    name_vacancy = models.CharField(max_length=255)
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55)
    date_born = models.DateField()
    email = models.EmailField()
    skills = models.CharField(max_length=55)
    professional_experience = models.CharField(max_length=55)
    education = models.CharField(max_length=55)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return f'{self.name_vacancy} - {self.name}'

    def get_absolute_url(self):
        return reverse('resume_slug', kwargs={'resume_slug': self.slug, 'pk': self.pk})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.name_vacancy}-{self.name}')
        super().save(force_insert, force_update, using, update_fields)
        return f'{self.name_vacancy} - {self.name}'
