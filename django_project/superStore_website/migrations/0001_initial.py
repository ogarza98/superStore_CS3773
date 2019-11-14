# Generated by Django 2.2.7 on 2019-11-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('freshness', models.CharField(choices=[('G', 'GOOD'), ('N', 'NEW'), ('B', 'BAD')], max_length=1)),
                ('item_stock', models.IntegerField()),
                ('price', models.FloatField()),
                ('goods_image', models.ImageField(blank=True, null=True, upload_to='goods_image')),
            ],
        ),
    ]
