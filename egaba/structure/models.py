from django.db import models
from django.shortcuts import reverse

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000, default='test')

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    class Meta:
        abstract = True

class University(CommonInfo):
    class Meta:
        verbose_name_plural = 'Universities'

    def get_absolute_url(self):
        return reverse('timeline:university', kwargs={'university': self.name})

class Faculty(CommonInfo):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university_faculty')

    class Meta:
        verbose_name_plural = 'Faculties'

    def get_absolute_url(self):
        return reverse('timeline:faculty', kwargs={
                    'university': self.university.name,
                    'faculty': self.name
                    })

class Department(CommonInfo):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="faculty_department")

    class Meta:
        verbose_name_plural = 'Departments'

    def get_absolute_url(self):
        return reverse('timeline:department', kwargs={
                    'university': self.faculty.university.name,
                    'faculty': self.faculty.name,
                    'department': self.name
                    })

class Subject(CommonInfo):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="department_subject")

    class Meta:
        verbose_name_plural = 'Subjects'

    def get_absolute_url(self):
        return reverse('timeline:subject', kwargs={
                    'university': self.department.faculty.university.name,
                    'faculty': self.department.faculty.name,
                    'department': self.department.name,
                    'subject': self.name
                    })
