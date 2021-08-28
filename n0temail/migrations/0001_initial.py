# Generated by Django 3.2.6 on 2021-08-23 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spf', models.CharField(max_length=254, null=True)),
                ('dkim', models.CharField(max_length=254, null=True)),
                ('html', models.TextField(null=True)),
                ('text', models.TextField(null=True)),
                ('subject', models.CharField(max_length=254, null=True)),
                ('headers', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('to_email', models.CharField(max_length=254, null=True)),
                ('charsets', models.JSONField()),
                ('envelope', models.JSONField()),
                ('sender_ip', models.CharField(max_length=254, null=True)),
                ('spam_score', models.FloatField(null=True)),
                ('from_email', models.CharField(max_length=254, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('spam_report', models.CharField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField()),
                ('path', models.CharField(max_length=254)),
                ('query', models.CharField(max_length=254)),
                ('method', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=254)),
                ('file', models.FileField(upload_to='attachments/')),
                ('filename', models.CharField(max_length=254)),
                ('content_id', models.CharField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='n0temail.email')),
            ],
        ),
    ]