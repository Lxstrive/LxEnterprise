import os
from datetime import datetime

from django.conf import settings
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import View
from django.views.decorators.http import require_POST, require_GET
from django.utils.timezone import make_aware

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from apps.news.models import NewsCategory, News, Banner
from .forms import EditNewsCategory, WriteNewsForm, AddBannerForm, \
    EditBannerForm, EditNewsForm, PubCourseForm
from utils import restful
from apps.news.serializers import BannerSerializer
from apps.course.models import Course, CourseCategory, Teacher


@staff_member_required(login_url='index')
def index(request):
    return render(request, 'cms/index.html')


class WriteNewsView(View):
    """
        发布新闻
    """

    def get(self, request):
        categories = NewsCategory.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'cms/write-news.html', context=context)

    def post(self, request):
        form = WriteNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            category = NewsCategory.objects.get(pk=category_id)
            News.objects.create(title=title, desc=desc, thumbnail=thumbnail,
                                content=content, category=category,
                                author=request.user)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())


@require_GET
def news_category(request):
    """
        新闻分类
    :param request:
    :return:
    """
    categories = NewsCategory.objects.all()
    return render(request, 'cms/news-category.html', {
        'categories': categories
    })


@require_POST
def add_news_category(request):
    """
        添加新闻分类
    :param request:
    :return:
    """
    name = request.POST.get('name', '')
    exists = NewsCategory.objects.filter(name=name).exists()
    if not exists:
        NewsCategory.objects.create(name=name)
        return restful.ok()
    else:
        return restful.params_error(message='该分类已存在')


@require_POST
def edit_news_category(request):
    """
    编辑新闻分类
    :param request:
    :return:
    """
    form = EditNewsCategory(request.POST)
    if form.is_valid():
        pk = form.cleaned_data.get('pk')
        name = form.cleaned_data.get('name')
        try:
            NewsCategory.objects.filter(pk=pk).update(name=name)
            return restful.ok()
        except:
            return restful.params_error(message='该分类不存在')
    else:
        return restful.params_error(message=form.get_error())


@require_POST
def delete_news_category(request):
    """
        删除新闻分类
    :param request:
    :return:
    """
    pk = request.POST.get('pk')
    try:
        NewsCategory.objects.filter(pk=pk).delete()
        return restful.ok()
    except:
        return restful.unauth(message='该分类不存在')


def banners(request):
    """
    轮播图
    :param request:
    :return:
    """
    return render(request, 'cms/banners.html')


def banner_list(request):
    """
    轮播图序列化
    :param request:
    :return:
    """
    banners = Banner.objects.all()
    serialize = BannerSerializer(banners, many=True)
    return restful.result(data=serialize.data)


def delete_banner(request):
    """
    删除轮播图
    :param request:
    :return:
    """
    banner_id = request.POST.get('banner_id')
    Banner.objects.filter(pk=banner_id).delete()
    return restful.ok()


def edit_banner(request):
    """
    编辑轮播图
    :param request:
    :return:
    """
    form = EditBannerForm(request.POST)
    if form.is_valid():
        pk = request.POST.get('pk')
        image_url = request.POST.get('image_url')
        link_to = request.POST.get('link_to')
        priority = request.POST.get('priority')
        Banner.objects.filter(pk=pk).update(image_url=image_url,
                                            link_to=link_to, priority=priority)
        return restful.ok()
    else:
        return restful.params_error(message=form.get_errors())


def add_banner(request):
    """
    添加轮播图
    :param request:
    :return:
    """
    form = AddBannerForm(request.POST)
    if form.is_valid():
        priority = request.POST.get('priority')
        image_url = request.POST.get('image_url')
        link_to = request.POST.get('link_to')
        banner = Banner.objects.create(priority=priority, image_url=image_url,
                                       link_to=link_to)
        return restful.result(data={'banner_id': banner.pk})
    else:
        return restful.params_error(message=form.get_errors())


@require_POST
def upload_file(request):
    """
        上传图片
    :param request:
    :return:
    """
    file = request.FILES.get('file')
    name = file.name
    with open(os.path.join(settings.MEDIA_ROOT, name), 'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url = request.build_absolute_uri(settings.MEDIA_URL + name)
    return restful.result(data={'url': url})


class NewsListView(View):
    """
        新闻列表
    """

    def get(self, request):
        categories = NewsCategory.objects.all()
        start = request.GET.get('start')
        end = request.GET.get('end')
        title = request.GET.get('title')
        category_id = int(request.GET.get('category', 0) or 0)
        news = News.objects.select_related('category', 'author')
        # 根据时间进行查询
        if start and end:
            if start:
                start_date = datetime.strptime(start, '%Y/%m/%d')
            else:
                start_date = datetime(year=2108, month=7, day=1)
            if end:
                end_date = datetime.strptime(end, '%Y/%m/%d')
            else:
                end_date = datetime.today()
            news = news.filter(
                pub_time__range={make_aware(start_date), make_aware(end_date)})
        # 根据标题进行查询
        if title:
            news = news.filter(title__icontains=title)
        # 根据分类尽心查询
        if category_id:
            news = news.filter(category=category_id)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(news, 2, request=request)
        newses = p.page(page)
        return render(request, 'cms/news_list.html', {
            'categories': categories,
            'newses': newses,
            'start': start,
            'end': end,
            'title': title,
            'category_id': category_id
        })


class EditNewsView(View):
    """
        编辑新闻
    """

    def get(self, request):
        news_id = request.GET.get('news_id')
        news = News.objects.get(pk=news_id)
        context = {
            'news': news,
            'categories': NewsCategory.objects.all()
        }
        return render(request, 'cms/write-news.html', context=context)

    def post(self, request):
        form = EditNewsForm(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            thumbnail = request.POST.get('thumbnail')
            content = request.POST.get('content')
            category_id = request.POST.get('category')
            pk = form.cleaned_data.get('pk')
            category = NewsCategory.objects.get(pk=category_id)
            News.objects.filter(pk=pk).update(title=title, desc=desc,
                                              thumbnail=thumbnail,
                                              content=content,
                                              category=category)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())


@require_POST
def delete_news(request):
    """
    删除新闻
    :param request:
    :return:
    """
    news_id = request.POST.get('news_id')
    News.objects.filter(pk=news_id).delete()
    return restful.ok()


class PubCourse(View):
    """
        发布课程
    """

    def get(self, request):
        context = {
            'categories': CourseCategory.objects.all(),
            'teachers': Teacher.objects.all()
        }
        return render(request, 'cms/public_course.html', context=context)

    def post(self, request):
        form = PubCourseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            category_id = form.cleaned_data.get('category_id')
            video_url = form.cleaned_data.get('video_url')
            cover_url = form.cleaned_data.get('cover_url')
            price = form.cleaned_data.get('price')
            duration = form.cleaned_data.get('duration')
            profile = form.cleaned_data.get('profile')
            teacher_id = form.cleaned_data.get('teacher_id')
            category = CourseCategory.objects.get(pk=category_id)
            teacher = Teacher.objects.get(pk=teacher_id)
            Course.objects.create(title=title, video_url=video_url,
                                  cover_url=cover_url, price=price,
                                  duration=duration, profile=profile,
                                  category=category, teacher=teacher)
            return restful.ok()
        else:
            return restful.params_error(message=form.get_errors())