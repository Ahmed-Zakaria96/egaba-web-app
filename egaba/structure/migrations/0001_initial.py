# Generated by Django 3.2.5 on 2021-08-15 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(default='test', max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(default='test', max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(default='test', max_length=1000)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_subject', to='structure.department')),
            ],
            options={
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(default='test', max_length=1000)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university_faculty', to='structure.university')),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_department', to='structure.faculty'),
        ),
    ]
