from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer_Info, Sex_Info, Cart_Info, Ad_Info, Camera_Info, Items
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import AdForm, CartForm, CouponForm, CameraForm, ItemForm, ItemsForm



@csrf_exempt
def coupon_check(request):
    if request.method == 'POST':
        request_data1 = ((request.body).decode('utf-8'))
        request_data = json.load(request_data1)




@csrf_exempt
def user_getinfo(request):
    if request.method == 'POST':
        request_data1 = ((request.body).decode('utf-8'))
        request_data = json.loads(request_data1)

        da = Customer_Info(request_data['id'], request_data['pw'], request_data['age'], request_data['sex'])
        da.save()

        return HttpResponse(request_data)


def cart_add(request):
    if request.method == 'POST':
        form = CartForm(request.POST)

        form_num = form.data['num']

        result_num = int(form_num)

        if result_num <= 0:
            return redirect('/admin/cart/cart_info/')

        total_num = Cart_Info.objects.count();

        i = 0
        while i < result_num:
            data = Cart_Info(num=total_num + i + 1)
            data.save()
            i = i + 1
    return redirect('/admin/cart/cart_info/')


def ad_add(request):
    if request.method == 'POST':
        form = AdForm(request.POST)

        form1 = form.data['item']
        form2 = form.data['camera_num']
        form3 = form.data['link_info']

        result_item = Items.objects.get(name=form1)
        result_camera = Camera_Info.objects.get(num=form2)

        numcount = Ad_Info.objects.count()+1

        data_ad = Ad_Info(num= numcount,item=result_item, camera_num=result_camera, link_info=form3)
        data_ad.save()
    return redirect('/admin/cart/ad_info/')


def coupon_add(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)

        form_name = form.data['name']
        form_item = form.data['item']
        form_discount_rate = form.data['discount_rate']
        form_end_date = form.data['end_date']
        form_inventory = form.data['inventory']

        result_name = form_name
        result_item = Items.objects.get(name=form_item)
        result_discount_rate = form_discount_rate
        result_end_date = form_end_date
        result_inventory = int(form_inventory)

        coupons = Coupons_Item(name=result_name, item=result_item, discount_rate=result_discount_rate,
                               end_date=result_end_date, inventory=result_inventory)
        coupons.save()


        i = 0
        while i < result_inventory:
            serial = User.objects.make_random_password(length=9, allowed_chars='1234567890')
            item = Coupons_Item.objects.get(item=result_item)
            use = False

            coupon_item = Coupon_Item_Info(serial_num=serial, coupon_item=item, coupon_use=use)
            coupon_item.save()
            i = i+1

    return redirect('/admin/cart/coupons_item/')


def camera_add(request):
    if request.method == 'POST':
        form = CameraForm(request.POST)

        form_num = form.data['num']

        result_num = int(form_num)

        if result_num <= 0:
            return redirect('/admin/cart/camera_info/')

        total_num = Camera_Info.objects.count()

        i = 0
        while i < result_num:
            data = Camera_Info(num=total_num+i+1)
            data.save()
            i = i+1

    return redirect('/admin/cart/camera_info/')


def item_add(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)

        form_item = form.data['item']
        form_inbound_date = form.data['inbound_date']
        form_expire_date = form.data['expire_date']
        form_inventory = form.data['num']

        result_item = Items.objects.get(name=form_item)
        result_inbound_date = form_inbound_date
        result_expire_date = form_expire_date
        result_inventory = int(form_inventory)

        if result_inventory <= 0:
            return redirect('/admin/cart/item_info/')

        total_num = Items.objects.get(name=result_item.name).inventory

        Items.objects.filter(name=result_item).update(inventory=total_num+result_inventory)

        i = 0
        while i < result_inventory:
            serial = User.objects.make_random_password(length=9, allowed_chars='1234567890')
            data = Item_Info(serial_num=serial, item=result_item, inbound_date=result_inbound_date, expire_date=result_expire_date)
            data.save()
            i = i+1

    return redirect('/admin/cart/item_info/')


def items_add(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)

        form_name = form.data['name']
        form_price = form.data['price']
        form_sort = form.data['sort']

        result_name = form_name
        result_price = form_price
        result_sort = Item_Sort_Info.objects.get(sort=form_sort)

        data = Items(name=result_name, price=result_price, sort=result_sort)
        data.save()

    return redirect('/admin/cart/items/')