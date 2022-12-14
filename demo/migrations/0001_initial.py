# Generated by Django 4.1.3 on 2022-11-16 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(default=None, max_length=120)),
            ],
            options={
                'verbose_name': 'Surname',
                'verbose_name_plural': 'Surnames',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=120)),
                ('person_dob', models.DateField()),
                ('initial_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Surnames', to='demo.surname')),
            ],
            options={
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
        ),
    ]
