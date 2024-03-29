# Generated by Django 3.1.5 on 2023-07-28 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0007_auto_20230119_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='resim',
            field=models.ImageField(blank=True, null=True, upload_to='yazi_resimleri'),
        ),
        migrations.AlterField(
            model_name='yazilarmodel',
            name='yazar',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='yazar', to=settings.AUTH_USER_MODEL),
        ),
    ]
