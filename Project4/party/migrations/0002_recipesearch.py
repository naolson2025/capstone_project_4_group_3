# Generated by Django 2.2.6 on 2019-10-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_search', models.CharField(max_length=200)),
            ],
        ),
    ]
