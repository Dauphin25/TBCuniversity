from django import forms
from university.models.Taking_Subjects import TakingSubjects
from university.models.assignment import Assignment
from university.models.course import Course


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class AssignmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None)
        super(AssignmentForm, self).__init__(*args, **kwargs)
        if professor:
            # Filter courses based on the professor
            self.fields['course'].queryset = Course.objects.filter(professor=professor)

    class Meta:
        model = Assignment
        fields = ['course', 'title', 'description', 'deadline']



class TakingSubjectsForm(forms.ModelForm):
    class Meta:
        model = TakingSubjects
        fields = ['student', 'course', 'semester']
        labels = {
            'student': 'Student',
            'course': 'Course',
            'semester': 'Semester'
        }
        widgets = {
            'semester': forms.NumberInput(attrs={'min': 1, 'max': 8})
        }