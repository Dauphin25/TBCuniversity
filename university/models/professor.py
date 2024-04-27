
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='professor', null=True, blank=True)
    first_name = models.CharField(max_length=100, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last Name'))
    email = models.EmailField(max_length=100, verbose_name=_('Email'), default='', blank=True)
    faculty = models.ForeignKey('university.Faculty', on_delete=models.CASCADE, related_name='professors',
                                verbose_name=_('Faculty'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Professor')
        verbose_name_plural = _('Professors')
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
