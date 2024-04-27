from django.db import models
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Course Name'))
    description = models.TextField(verbose_name=_('Description'))
    professor = models.ForeignKey('university.Professor', on_delete=models.CASCADE, related_name='courses',
                                  verbose_name=_('Professor'), blank=True, null=True)
    syllabus = models.FileField(upload_to='university/syllabus/', verbose_name=_('Syllabus'))
    number_of_credits = models.PositiveIntegerField(verbose_name=_('Number of Credits'), default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
