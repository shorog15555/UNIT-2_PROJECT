# Generated by Django 4.2.1 on 2023-06-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048)),
                ('description', models.TextField()),
                ('image', models.URLField()),
                ('vedio', models.URLField()),
            ],
        ),
    ]
