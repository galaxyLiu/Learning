# Generated by Django 2.2.6 on 2021-03-14 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_banner_hotsearchwords_indexad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscategorybrand',
            name='catagory',
        ),
        migrations.AddField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brands', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]