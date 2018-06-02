# Generated by Django 2.0.4 on 2018-05-13 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20180510_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad_info',
            name='camera_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Camera_Info'),
        ),
        migrations.AlterField(
            model_name='ad_info',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Items'),
        ),
        migrations.AlterField(
            model_name='cart_info',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info'),
        ),
        migrations.AlterField(
            model_name='coupon_item_info',
            name='coupon_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Coupons_Item'),
        ),
        migrations.AlterField(
            model_name='coupon_item_info',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info'),
        ),
        migrations.AlterField(
            model_name='coupon_sort_info',
            name='coupon_sorts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Coupons_Sort'),
        ),
        migrations.AlterField(
            model_name='coupon_sort_info',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info'),
        ),
        migrations.AlterField(
            model_name='coupons_item',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Items'),
        ),
        migrations.AlterField(
            model_name='coupons_sort',
            name='sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Item_Sort_Info'),
        ),
        migrations.AlterField(
            model_name='customer_info',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Sex_Info'),
        ),
        migrations.AlterField(
            model_name='item_info',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Items'),
        ),
        migrations.AlterField(
            model_name='items',
            name='sort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Item_Sort_Info'),
        ),
        migrations.AlterField(
            model_name='mv_history',
            name='camera_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Camera_Info'),
        ),
        migrations.AlterField(
            model_name='mv_history',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info'),
        ),
        migrations.AlterField(
            model_name='pur_history',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Customer_Info'),
        ),
        migrations.AlterField(
            model_name='pur_history',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.Item_Info'),
        ),
    ]
