# Generated by Django 2.2.3 on 2019-07-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.UUIDField()),
                ('status', models.CharField(choices=[('COMPLETE', 'Complete'), ('FAILED', 'Failed'), ('PENDING', 'Pending'), ('OTHER', 'Other')], default='PENDING', max_length=8)),
                ('task_name', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=255)),
                ('date_complete', models.DateTimeField()),
            ],
        ),
    ]
