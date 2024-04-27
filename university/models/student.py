from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='student', null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    email = models.EmailField(max_length=100, verbose_name=_('Email'), default='', blank=True)
    gpa = models.FloatField(
        verbose_name='GPA',
        validators=[MaxValueValidator(4.0)],
        default=0.0
    )
    faculty = models.ForeignKey('university.Faculty', on_delete=models.CASCADE, related_name='students',
                                verbose_name=_('Faculty'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
