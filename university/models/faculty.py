from django.db import models
from django.utils.translation import gettext_lazy as _
from university.models.professor import Professor
from university.models.course import Course


class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Faculty Name'))
    description = models.TextField(verbose_name=_('Description'))
    email = models.EmailField(max_length=100, verbose_name=_('Email'), default='', blank=True)
    courses = models.ManyToManyField(Course, related_name='faculties', verbose_name=_('Courses'), blank=True)

    head_of_faculty = models.OneToOneField(
        Professor,
        on_delete=models.SET_NULL,
        related_name='faculty_head',  # Custom related_name for the head_of_faculty field
        null=True,
        blank=True,
        verbose_name=_('Head of Faculty')
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Faculty')
        verbose_name_plural = _('Faculties')
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
