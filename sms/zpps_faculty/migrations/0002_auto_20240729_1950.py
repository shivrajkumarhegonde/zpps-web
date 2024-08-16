# Generated by Django 3.2.25 on 2024-07-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zpps_faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultymember',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='faculty_images/'),
        ),
        migrations.AlterField(
            model_name='facultymember',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='facultymember',
            name='position',
            field=models.CharField(max_length=100),
        ),
    ]
