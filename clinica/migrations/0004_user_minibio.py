# Generated by Django 5.1.2 on 2024-10-16 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0003_solicitacaoatendimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='minibio',
            field=models.CharField(db_column='minibio', max_length=800, null=True),
        ),
    ]
