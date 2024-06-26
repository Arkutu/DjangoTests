# Generated by Django 5.0.6 on 2024-06-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customusergroups',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customuseruserpermissions',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customusergroups',
            name='group',
        ),
        migrations.RemoveField(
            model_name='customuseruserpermissions',
            name='permission',
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='CustomUserGroups',
        ),
        migrations.DeleteModel(
            name='CustomUserUserPermissions',
        ),
    ]
