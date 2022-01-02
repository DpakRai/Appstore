# Generated by Django 3.2.5 on 2021-08-03 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]