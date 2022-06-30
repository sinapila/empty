# Generated by Django 4.0.3 on 2022-06-29 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_remove_productbrand_url_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='productbrand',
            name='url_title',
            field=models.CharField(db_index=True, default='digedige', max_length=300, verbose_name='عنوان در url'),
            preserve_default=False,
        ),
    ]