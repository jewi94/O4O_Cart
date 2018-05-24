from datetime import date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Sex_Info(models.Model):
    class Meta:
        verbose_name_plural="성별"
        verbose_name="성별"
    sex = models.CharField(max_length=20, null=False, primary_key=True, default="", verbose_name='성별')


class Customer_Info(models.Model):
    class Meta:
        verbose_name_plural="고객정보"
        verbose_name="고객정보"
    id = models.CharField(max_length=15, null=False, primary_key=True, default="", verbose_name='아이디')
    pwd = models.CharField(max_length=15, null=False, verbose_name='비밀번호')
    age = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(200),
            MinValueValidator(0)
        ], default=0, verbose_name='나이')
    sex = models.ForeignKey(Sex_Info, on_delete=models.SET_NULL, null=True, verbose_name='성별')
    note = models.TextField(max_length=1000, null=True, blank=True, default="", verbose_name='비고')


class Cart_Info(models.Model):
    class Meta:
        verbose_name_plural="카트"
        verbose_name="카트"
    num = models.PositiveIntegerField(primary_key=True, null=False, verbose_name='추가할 카트수')
    #num = models.AutoField(primary_key=True, null=False, default=1, verbose_name='카트번호')
    owner = models.ForeignKey(Customer_Info, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='소유자')




class Item_Sort_Info(models.Model):
    class Meta:
        verbose_name_plural="상품종류"
        verbose_name="상품종류"
    sort = models.CharField(max_length=100, primary_key=True, null=False, default="", verbose_name='상품종류')


class Items(models.Model):
    class Meta:
        verbose_name_plural="상품"
        verbose_name="상품"
    name = models.CharField(max_length=15, primary_key=True, default="", null=False, verbose_name='상품명')
    inventory = models.PositiveSmallIntegerField(null=False, verbose_name='재고')
    price = models.PositiveIntegerField(null=False, verbose_name='가격')
    sort = models.ForeignKey(Item_Sort_Info, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='상품종류')


class Item_Info(models.Model):
    class Meta:
        verbose_name_plural="상품 재고"
        verbose_name="상품 재고"
    serial_num = models.AutoField(primary_key=True, default=1, verbose_name='일련번호')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False, verbose_name='상품')
    inbound_date = models.DateField(verbose_name='입고일', null=False, default=date.today)
    expire_date = models.DateField(verbose_name='유통기한', null=False, default=date.today)



class Camera_Info(models.Model):
    class Meta:
        verbose_name_plural="카메라"
        verbose_name="카메라"
    num = models.PositiveSmallIntegerField(primary_key=True, default=0, null=False, verbose_name='추가할 카메라수')


class Pur_History(models.Model):
    class Meta:
        verbose_name_plural="고객 구매정보"
        verbose_name = "고객 구매정보"
    num = models.AutoField(primary_key=True, default=1, verbose_name='번호')
    customer = models.ForeignKey(Customer_Info, on_delete=models.CASCADE, null=False, verbose_name='구매고객')
    time = models.DateTimeField(auto_now_add=True, verbose_name='구매시간')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False, verbose_name='구매상품')


class Mv_History(models.Model):
    class Meta:
        verbose_name_plural="고객 이동정보"
        verbose_name="고객 이동정보"
    num = models.AutoField(primary_key=True, default=1, verbose_name='번호')
    customer = models.ForeignKey(Customer_Info, on_delete=models.CASCADE, null=False, verbose_name='이동고객')
    time = models.DateTimeField(auto_now_add=True, verbose_name='이동한 시간')
    camera_num = models.ForeignKey(Camera_Info, on_delete=models.CASCADE, null=False, verbose_name='카메라 번호')


class Ad_Info(models.Model):
    class Meta:
        verbose_name_plural="광고"
        verbose_name="광고"
    num = models.AutoField(primary_key=True, default=1, verbose_name='번호')
    #num = models.PositiveIntegerField(primary_key=True, null=False, verbose_name='번호', default=1)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False, verbose_name='구매상품')
    camera_num = models.ForeignKey(Camera_Info, on_delete=models.CASCADE, null=False, verbose_name='카메라 번호')
    link_info = models.CharField(max_length=200, null=False, verbose_name='광고영상 링크')


class Coupons_Item(models.Model):
    class Meta:
        verbose_name_plural="상품 쿠폰"
        verbose_name="상품 쿠폰"
    name = models.CharField(max_length=15, null=False, primary_key=True, default="", verbose_name='쿠폰이름')
    item = models.ForeignKey(Items, on_delete=models.CASCADE, null=False, verbose_name='쿠폰이 적용된 상품')
    discount_rate = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ], default=0, null=False, verbose_name='할인률')
    end_date = models.DateField(default=date.today, null=False, verbose_name='종료일')
    inventory = models.PositiveSmallIntegerField(null=False, verbose_name='발매개수')


class Coupon_Item_Info(models.Model):
    class Meta:
        verbose_name_plural="상품 쿠폰 재고"
        verbose_name="상품 쿠폰 재고"
    serial_num = models.PositiveIntegerField(primary_key=True, default=1, editable=False, verbose_name='일련번호') # 9자리까지 가능
    coupon_item = models.ForeignKey(Coupons_Item, on_delete=models.CASCADE, null=False, verbose_name='쿠폰이름')
    coupon_use = models.BooleanField(null=False, default=False, verbose_name='사용여부')
    customer = models.ForeignKey(Customer_Info, on_delete=models.CASCADE, null=True, blank=True, verbose_name='소유자')



'''
class Coupons_Sort(models.Model):
    class Meta:
        verbose_name_plural="상품 종류 쿠폰"
    name = models.CharField(max_length=15, null=False, primary_key=True, default=0, verbose_name='쿠폰이름')
    sort = models.ForeignKey(Item_Sort_Info, on_delete=models.CASCADE, null=False, verbose_name='쿠폰이 적용된 상품종류')
    discount_rate = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ], default=0, null=False, verbose_name='할인률')
    release_date = models.DateField(default=date.today, null=False, verbose_name='발매일')
    end_date = models.DateField(default=date.today, null=False, verbose_name='종료일')
    inventory = models.PositiveSmallIntegerField(null=False, verbose_name='발매개수')


class Coupon_Sort_Info(models.Model):
    class Meta:
        verbose_name_plural="상품 종류 쿠폰"
    serial_num = models.AutoField(primary_key=True, default=1, verbose_name='일련번호')
    coupon_sorts = models.ForeignKey(Coupons_Sort, on_delete=models.CASCADE, null=False, verbose_name='쿠폰이름')
    coupon_use = models.BooleanField(null=False, default=False, verbose_name='사용여부')
    customer = models.ForeignKey(Customer_Info, on_delete=models.CASCADE, null=False, verbose_name='소유자')
'''