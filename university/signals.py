from django.db.models.signals import pre_save
from django.dispatch import receiver
from university.models.faculty import Faculty
from university.models.professor import Professor
from university.models.student import Student
from django.contrib.auth.models import User
from django.db.models.signals import post_save


@receiver(pre_save, sender=Faculty)
def generate_email_for_faculty(sender, instance, **kwargs):
    if instance.email == '' or instance.email is None:
        print("Signal handler function is being called!")
        username = instance.name.lower().replace(' ', '-') + '@tbc.edu.ge'
        instance.email = username


@receiver(pre_save, sender=Professor)
def generate_email_for_professor(sender, instance, **kwargs):
    if not instance.email:
        username = f'{instance.first_name.lower()}.{instance.last_name.lower()}@tbc.edu.ge'
        instance.email = username


@receiver(pre_save, sender=Student)
def generate_email_for_student(sender, instance, **kwargs):
    if not instance.email:
        username = f'{instance.first_name.lower()}.{instance.last_name.lower()}@tbc.edu.ge'
        instance.email = username


# Define receiver functions for Professor and Student
@receiver(pre_save, sender=Professor)
def create_or_update_professor_user(sender, instance, **kwargs):
    if instance.pk:  # Check if the instance has a primary key (i.e., it's not a new object)
        # Object is being updated
        user = instance.user
        if user:  # Check if the professor has an associated user account
            # Update user account details
            user.email = instance.email
            user.first_name = instance.first_name
            user.last_name = instance.last_name
            user.save()
        else:
            # Create a new user account
            username = instance.first_name.lower() + instance.last_name.lower()  # Generate username
            email = instance.email
            password = 'password'  # Set your default password here
            user = User.objects.create_user(username=username, email=email, password=password)
            instance.user = user


@receiver(pre_save, sender=Student)
def create_or_update_student_user(sender, instance, **kwargs):
    if instance.pk:  # Check if the instance has a primary key (i.e., it's not a new object)
        # Object is being updated
        user = instance.user
        if user:  # Check if the student has an associated user account
            # Update user account details
            user.email = instance.email
            user.first_name = instance.first_name
            user.last_name = instance.last_name
            user.save()
        else:
            # Create a new user account
            username = instance.first_name.lower() + instance.last_name.lower()  # Generate username
            email = instance.email
            password = 'password'  # Set your default password here
            user = User.objects.create_user(username=username, email=email, password=password)
            instance.user = user