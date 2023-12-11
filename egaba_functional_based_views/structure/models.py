from django.db import models

# Create your models here.
# university/faculty/department/level/sbject models
class University(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Universities'

class Faculty(models.Model):
    name = models.CharField(max_length=80)
    university = models.ManyToManyField(University, related_name="university_faculty")

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    class Meta:
        verbose_name_plural = 'Faculties'

class Department(models.Model):
    name = models.CharField(max_length=80)
    faculty = models.ManyToManyField(Faculty, related_name="faculty_department")

    def __str__(self):
        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    class Meta:
        verbose_name_plural = 'Departments'

class Level(models.Model):
    name = models.CharField(max_length=80)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="department_level")

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=80)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="level_subject", default=None, null=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subjects'
