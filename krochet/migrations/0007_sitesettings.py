# Generated by Django 4.1.6 on 2023-02-17 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('krochet', '0006_order_completed'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title', max_length=20, verbose_name='Title')),
                ('subTitle', models.CharField(default='Sub title', max_length=50, verbose_name='Sub Title')),
                ('about', models.TextField(default='About Me', verbose_name='About me')),
                ('featured', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krochet.crochet', verbose_name='Featured Product')),
            ],
        ),
    ]
