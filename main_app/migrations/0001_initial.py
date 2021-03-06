# Generated by Django 3.2.7 on 2021-09-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('colorway', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('4', '4'), ('4.5', '4.5'), ('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9'), ('8.5', '9.5'), ('9.5', '8.5'), ('10', '10'), ('10.5', '10.5'), ('11', '1'), ('11.5', '11.5'), ('12', '12'), ('12.5', '12.5')], default='4', max_length=20)),
            ],
        ),
    ]
