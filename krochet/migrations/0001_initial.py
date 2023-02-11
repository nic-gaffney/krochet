# Generated by Django 4.1.6 on 2023-02-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crochet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('picture', models.ImageField(upload_to='static/images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('info', models.TextField()),
            ],
        ),
    ]