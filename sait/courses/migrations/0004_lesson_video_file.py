# Generated by Django 4.2.7 on 2023-11-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lesson_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='video_file',
            field=models.FileField(default=1, upload_to='videos'),
            preserve_default=False,
        ),
    ]
