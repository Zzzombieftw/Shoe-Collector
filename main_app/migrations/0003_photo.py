# Generated by Django 3.2.7 on 2021-09-09 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_shoe_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('shoe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.shoe')),
            ],
        ),
    ]
