# Generated by Django 4.2.6 on 2023-10-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoryType',
            field=models.CharField(choices=[('NW', 'News'), ('AR', 'Article')], default='AR', max_length=20),
        ),
    ]