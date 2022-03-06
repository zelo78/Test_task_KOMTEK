# Generated by Django 4.0.3 on 2022-03-06 12:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceIdentifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=64, unique=True, verbose_name='идентификатор справочника')),
            ],
            options={
                'verbose_name': 'идентификатор справочника',
                'verbose_name_plural': 'идентификаторы справочников',
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='наименование справочника')),
                ('short_name', models.CharField(max_length=128, verbose_name='краткое наименование справочника')),
                ('description', models.TextField(verbose_name='описание справочника')),
                ('version', models.CharField(max_length=32, verbose_name='версия справочника')),
                ('valid_from', models.DateField(default=datetime.date.today, verbose_name='дата начала действия')),
                ('identifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='main.resourceidentifier', verbose_name='идентификатор')),
            ],
            options={
                'verbose_name': 'Справочник',
                'verbose_name_plural': 'Справочники',
                'ordering': ['-valid_from'],
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64, verbose_name='код элемента')),
                ('value', models.CharField(max_length=256, verbose_name='значение элемента')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='main.resource', verbose_name='справочник')),
            ],
            options={
                'verbose_name': 'Элемент справочника',
                'verbose_name_plural': 'Элементы справочника',
                'ordering': ['code'],
            },
        ),
        migrations.AddConstraint(
            model_name='resource',
            constraint=models.UniqueConstraint(fields=('identifier', 'version'), name='unique_version_for_identifier'),
        ),
    ]
