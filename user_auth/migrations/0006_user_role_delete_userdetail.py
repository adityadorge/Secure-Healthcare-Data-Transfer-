# Generated by Django 5.0.3 on 2024-04-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0005_alter_userdetail_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='patient', max_length=50),
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]