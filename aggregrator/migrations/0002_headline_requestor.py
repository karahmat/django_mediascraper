# Generated by Django 4.0 on 2021-12-30 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('aggregrator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='requestor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
