# Generated by Django 4.2 on 2024-09-23 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.IntegerField(blank=True, default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('full_name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('position_id', models.IntegerField(blank=True, default=1, verbose_name='Позиция')),
                ('room', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ipphone_app.department')),
            ],
        ),
    ]
