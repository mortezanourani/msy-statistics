# Generated by Django 4.2 on 2024-12-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building_Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='License_Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='city',
            name='province',
        ),
        migrations.DeleteModel(
            name='Province',
        ),
    ]