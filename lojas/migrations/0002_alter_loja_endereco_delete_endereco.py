# Generated by Django 4.1.4 on 2023-01-10 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lojas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loja',
            name='endereco',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]
