# Generated by Django 4.0.3 on 2022-03-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(blank=True, max_length=75, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]