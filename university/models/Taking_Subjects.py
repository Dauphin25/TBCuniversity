from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from university.models import Student, Course
from django.utils.translation import gettext_lazy as _


class TakingSubjects(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_subjects',
                                 verbose_name=_('Student'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students_taking',
                               verbose_name=_('Course'))
    semester = models.PositiveIntegerField(verbose_name=_('Semester'), default=1,
                                           validators=[MinValueValidator(1), MaxValueValidator(8)])  # Assuming a semester range from 1 to 8
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Taking Subject')
        verbose_name_plural = _('Taking Subjects')
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.student} - {self.course}'
