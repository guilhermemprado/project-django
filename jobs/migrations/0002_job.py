# Generated by Django 4.2 on 2023-04-27 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('responsibilities', models.TextField()),
                ('level', models.CharField(choices=[('jr', 'Júnior'), ('pl', 'Pleno'), ('sr', 'Sênior')], max_length=2)),
                ('skills', models.ManyToManyField(related_name='jobs', to='jobs.skill')),
            ],
        ),
    ]
