# Generated by Django 5.0.7 on 2024-08-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_banner_alter_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
