# Generated by Django 2.0.1 on 2019-03-08 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20190308_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_brand', models.IntegerField(default=0)),
                ('name', models.CharField(default=0, max_length=400)),
            ],
        ),
    ]
