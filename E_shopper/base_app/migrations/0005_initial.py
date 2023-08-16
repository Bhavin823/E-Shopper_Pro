# Generated by Django 4.2 on 2023-08-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_app', '0004_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parents', models.ManyToManyField(blank=True, related_name='children', to='base_app.category')),
            ],
        ),
    ]