# Generated by Django 4.1.5 on 2024-05-03 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=150, unique=True)),
                ('plan', models.CharField(max_length=100)),
                ('available_tokens', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=150)),
            ],
        ),
    ]
