
from django.utils.translation import gettext_lazy as _
from django.db import models
from university.models.student import Student
from university.models.course import Course


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances',
                                 verbose_name=_('Student'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendances',
                               verbose_name=_('Course'))
    date = models.DateField(verbose_name=_('Date'))
    is_present = models.BooleanField(default=True, verbose_name=_('Is Present'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Attendance')
        verbose_name_plural = _('Attendances')
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.student} - {self.course} - {self.date}'