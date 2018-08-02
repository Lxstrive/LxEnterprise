from django.db import models
from shortuuidfield import ShortUUIDField


class CourseCategory(models.Model):
    """
        课程分类
    """
    name = models.CharField(max_length=100)


class Teacher(models.Model):
    """
        教师表
    """
    username = models.CharField(max_length=100)
    avatar = models.URLField()
    job_title = models.CharField(max_length=100)
    profile = models.TextField()


class Course(models.Model):
    """
        课程表
    """
    title = models.CharField(max_length=200)
    category = models.ForeignKey('CourseCategory', on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING)
    video_url = models.URLField()
    cover_url = models.URLField()
    price = models.FloatField()
    duration = models.IntegerField()
    profile = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)


class CourseOrder(models.Model):
    """
        课程订单页面
    """
    uid = ShortUUIDField(primary_key=True)
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING)
    # 购买用户
    buyer = models.ForeignKey('userauth.User', on_delete=models.DO_NOTHING)
    # 金额
    amount = models.FloatField(default=0)
    pub_time = models.DateTimeField(auto_now_add=True)
    # 订单类型(1.支付宝、2.微信)
    istype = models.SmallIntegerField(default=0)
    # 订单状态(1.未支付、2.已支付)
    status = models.SmallIntegerField(default=1)