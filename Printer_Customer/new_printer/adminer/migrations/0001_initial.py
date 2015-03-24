# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('shop_count', models.IntegerField()),
                ('city_pv', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=15)),
                ('register_time', models.DateTimeField()),
                ('last_login_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('icon', models.ImageField(upload_to=b'')),
                ('icon_url', models.URLField()),
                ('register_time', models.DateTimeField()),
                ('last_login_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('scan_count', models.IntegerField()),
                ('modified_time', models.DateTimeField()),
                ('describe', models.TextField()),
                ('marked_count', models.IntegerField()),
                ('tags', models.CharField(max_length=255)),
                ('is_published', models.BooleanField(default=b'false')),
                ('stl_file_url', models.URLField()),
                ('preview_1', models.ImageField(upload_to=b'')),
                ('preview_2', models.ImageField(upload_to=b'')),
                ('preview_3', models.ImageField(upload_to=b'')),
                ('preview_url_1', models.URLField()),
                ('preview_url_2', models.URLField()),
                ('preview_url_3', models.URLField()),
                ('add_time', models.DateTimeField()),
                ('designer', models.OneToOneField(to='adminer.Designer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('states', models.CharField(max_length=30)),
                ('add_time', models.DateTimeField()),
                ('customer', models.ForeignKey(to='adminer.Customer')),
                ('goods', models.ForeignKey(to='adminer.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tags', models.CharField(max_length=255)),
                ('describe', models.TextField()),
                ('build_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=100)),
                ('score', models.FloatField()),
                ('company_name', models.CharField(max_length=100)),
                ('describe', models.TextField()),
                ('icon', models.ImageField(upload_to=b'')),
                ('icon_url', models.URLField()),
                ('register_time', models.DateTimeField()),
                ('last_login_time', models.DateTimeField()),
                ('city', models.OneToOneField(to='adminer.City')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(to='adminer.Shop'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designer',
            name='reservation_list',
            field=models.ManyToManyField(to='adminer.Reservation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designer',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='cart',
            field=models.ManyToManyField(related_name='customer_wish_goods', to='adminer.Goods'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='collect_list',
            field=models.ManyToManyField(related_name='customer_collect_goods', to='adminer.Goods'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='marked_designers',
            field=models.ManyToManyField(to='adminer.Designer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='purchased_list',
            field=models.ManyToManyField(related_name='customer_purchase_goods', to='adminer.Goods'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='reservation',
            field=models.OneToOneField(to='adminer.Reservation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
