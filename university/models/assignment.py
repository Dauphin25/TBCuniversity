from django.db import models
from django.utils.translation import gettext_lazy as _
from university.models.course import Course


class Assignment(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Assignment Title'))
    description = models.TextField(verbose_name=_('Description'))
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='assignments',
                               verbose_name=_('Course'), blank=True, null=True)
    deadline = models.DateTimeField(verbose_name=_('Deadline'))
    points = models.PositiveIntegerField(verbose_name=_('Points'), default=0)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))

    class Meta:
        verbose_name = _('Assignment')
        verbose_name_plural = _('Assignments')
        ordering = ('-created_at',)

    def __str__(self):
        return self.title
