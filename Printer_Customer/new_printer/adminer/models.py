# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User


# 城市
class City(models.Model):
    # 城市名
    name            = models.CharField(max_length = 30)
    # 该城市打印店总数
    shop_count      = models.IntegerField()
    # 该城市总访问量（PV：visitor volume）
    city_pv         = models.IntegerField();


# 预约订单（预约设计师）
class Reservation(models.Model):
    # 商品标签（暂定为每个商品可以指定3个标签）
    tags            = models.CharField(max_length = 255)
    # 描述信息
    describe        = models.TextField()
    # 创建时间
    build_date      = models.DateTimeField()

    
# 设计师
class Designer(models.Model):
    # user扩展
    user                = models.OneToOneField(User);
    # 头像（暂时将图片保存在数据库中）
    icon                = models.ImageField();
    # 头像图片URL（暂时没有使用，待以后扩展）
    icon_url            = models.URLField();
    # 打印预约订单列表
    reservation_list    = models.ManyToManyField(Reservation)
    # 注册时间
    register_time       = models.DateTimeField();
    # 上次登录时间
    last_login_time     = models.DateTimeField();
    
    
# 商品
class Goods(models.Model):
    # 商品名称
    name                = models.CharField(max_length = 50)
    # 商品价格
    price               = models.FloatField()
    # 该商品对应的设计师
    designer            = models.OneToOneField(Designer)
    # 用户浏览该商品的次数
    scan_count          = models.IntegerField()
    # 上次修改时间
    modified_time       = models.DateTimeField()
    #　商品描述
    describe            = models.TextField()
    # 该商品被用户收藏次数
    marked_count        = models.IntegerField()
    # 商品标签
    tags                = models.CharField(max_length = 255)
    # 该商品是否已经发布（只有发布的商品才能在商店中显示）
    is_published        = models.BooleanField(default = "false")
    # STL3D模型的url
    stl_file_url        = models.URLField()
    # 预览图片1（3D模型预览，目前直接存放在数据库中）
    preview_1           = models.ImageField()
    preview_2           = models.ImageField()
    preview_3           = models.ImageField()
    # 预览图片URL（暂时未使用）
    preview_url_1       = models.URLField()
    preview_url_2       = models.URLField()
    preview_url_3       = models.URLField()
    # 创建时间
    add_time            = models.DateTimeField()


# 用户
class Customer(models.Model):
    # user扩展
    user                = models.OneToOneField(User)
    # 电话
    phone               = models.CharField(max_length = 15)
    # 已购商品
    purchased_list      = models.ManyToManyField(Goods, related_name = "customer_purchase_goods")
    # 购物车
    cart                = models.ManyToManyField(Goods, related_name = "customer_wish_goods")
    # 收藏列表
    collect_list        = models.ManyToManyField(Goods, related_name = "customer_collect_goods")
    # 预约设计师订单
    reservation         = models.OneToOneField(Reservation)
    # 关注的设计师列表
    marked_designers    = models.ManyToManyField(Designer)
    # 注册时间
    register_time       = models.DateTimeField()
    # 上次登录时间
    last_login_time     = models.DateTimeField()
    

# 打印服务供应商
class Shop(models.Model):
    # user扩展
    user                = models.OneToOneField(User)
    # 所在城市
    city                = models.OneToOneField(City)
    # 地址
    address             = models.CharField(max_length = 100)
    # 店家星级
    score               = models.FloatField();
    # 公司名称 
    company_name        = models.CharField(max_length = 100)
    # 公司简介
    describe            = models.TextField()
    # 公司图片（暂时将图片保存在数据库中）
    icon                = models.ImageField()
    # 公司图片URL（暂时没有使用，待以后扩展）
    icon_url            = models.URLField();
    # 注册时间 
    register_time       = models.DateTimeField()
    # 上次登录时间
    last_login_time     = models.DateTimeField()
    

# 商家打印订单（该订单由用户指派给商家）
class Order(models.Model):
    # 该订单对应的商店
    shop                = models.ForeignKey(Shop)
    # 该订单对应的商品
    goods               = models.ForeignKey(Goods)
    # 该订单对应的客户
    customer            = models.ForeignKey(Customer)
    # 该订单的状态
    states              = models.CharField(max_length = 30)
    # 订单提交时间
    add_time            = models.DateTimeField();
    
    
    
