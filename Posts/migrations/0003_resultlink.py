# Generated by Django 2.2 on 2020-04-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_auto_20200422_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_text', models.CharField(max_length=200)),
                ('link_tag', models.CharField(max_length=100)),
            ],
        ),
    ]
