# Generated by Django 5.0.7 on 2024-09-28 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artisanprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='artisanprofile',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='artisanprofile',
            name='total_reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artisanprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, to='profiles.skill'),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('artisan_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='profiles.artisanprofile')),
            ],
        ),
    ]