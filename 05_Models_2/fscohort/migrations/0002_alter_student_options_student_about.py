# Generated by Django 4.1.4 on 2022-12-12 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name': 'ögrenci', 'verbose_name_plural': 'Ögrenciler'},
        ),
        migrations.AddField(
            model_name='student',
            name='about',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
