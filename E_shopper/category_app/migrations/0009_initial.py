# Generated by Django 4.2 on 2023-08-16 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category_app', '0008_remove_subcategorymodel_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=100, unique=True)),
                ('categoryImage', models.ImageField(blank=True, upload_to='category')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategoryName', models.CharField(max_length=100)),
                ('subcategoryImage', models.ImageField(blank=True, upload_to='subcategory')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category_app.categorymodel')),
            ],
        ),
    ]
