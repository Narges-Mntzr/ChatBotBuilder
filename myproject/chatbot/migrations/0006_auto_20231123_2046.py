# Generated by Django 3.2.12 on 2023-11-23 17:16

from django.db import migrations, models
import django.db.models.deletion
import pgvector.django


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_enable_pgvector'),
    ]

    operations = [
        migrations.AddField(
            model_name='botcontent',
            name='embedding',
            field=pgvector.django.VectorField(dimensions=1536, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='related_botcontent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chatbot.botcontent'),
        ),
    ]
