# Generated by Django 3.0.6 on 2020-07-16 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('gf', models.CharField(max_length=256)),
                ('bf', models.CharField(max_length=256)),
            ],
        ),
    ]
