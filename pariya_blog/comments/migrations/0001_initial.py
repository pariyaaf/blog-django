# Generated by Django 5.0.6 on 2024-06-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=200)),
                ('commet_date', models.DateTimeField(auto_now_add=True)),
                ('post_id', models.IntegerField()),
                ('comment_text', models.TextField()),
            ],
        ),
    ]
