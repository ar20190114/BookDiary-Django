# Generated by Django 3.1 on 2021-09-10 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
                ('comment', models.TextField()),
                ('endday', models.DateField()),
            ],
        ),
    ]
