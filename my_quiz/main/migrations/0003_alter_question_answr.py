# Generated by Django 3.2.5 on 2021-07-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_question_answr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answr',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=5, verbose_name='Ответ'),
        ),
    ]
