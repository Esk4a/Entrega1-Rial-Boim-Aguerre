# Generated by Django 2.2.12 on 2022-05-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfinal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Facebook', models.CharField(max_length=40)),
                ('Telefono', models.IntegerField()),
            ],
        ),
    ]