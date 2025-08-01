# Generated by Django 5.2.3 on 2025-07-30 07:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_knowledgepoint_brief_desc'),
        ('user_systems', '0004_course_coursedata_currentcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='estim_duration',
            field=models.DurationField(),
        ),
        migrations.CreateModel(
            name='UserKnowledgeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(0, 'Unseen'), (1, 'Seen'), (2, 'Practised'), (3, 'Applied'), (4, 'Mastered')])),
                ('updated_on', models.DateTimeField()),
                ('kp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.knowledgepoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserKnowledgeUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(0, 'Unseen'), (1, 'Seen'), (2, 'Practised'), (3, 'Applied'), (4, 'Mastered')])),
                ('anticheat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.activity')),
                ('kp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.knowledgepoint')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
