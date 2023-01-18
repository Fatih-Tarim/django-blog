# Generated by Django 3.1.5 on 2023-01-18 11:57

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0002_auto_20230118_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='YazilarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resim', models.ImageField(upload_to='yazi_resimleri')),
                ('baslik', models.CharField(max_length=50)),
                ('icerik', models.TextField()),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('duzenlenme_tarihi', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='baslik', unique=True)),
                ('kategoriler', models.ManyToManyField(related_name='yazilar', to='blogapp.KategoriModel')),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yazar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Yazi',
                'verbose_name_plural': 'Yazilar',
                'db_table': 'Yazi',
            },
        ),
    ]
