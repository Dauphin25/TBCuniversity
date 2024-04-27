# Generated by Django 5.0.4 on 2024-04-23 20:55

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0002_alter_faculty_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number_of_credits',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Number of Credits'),
        ),
        migrations.AlterField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='university.professor', verbose_name='Professor'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='faculties', to='university.course', verbose_name='Courses'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professors', to='university.faculty', verbose_name='Faculty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='university.faculty', verbose_name='Faculty'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MaxValueValidator(4.0)], verbose_name='GPA'),
        ),
    ]
