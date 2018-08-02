from django.shortcuts import render
from django.conf import settings
from django.http import Http404

from .serializers import NewsSerializer, CommentSerializer

from .models import News, NewsCategory, Comment, Banner
from .forms import PublicCommentForm
from utils import restful
from apps.userauth.decorators import user_login_required


def index(request):
    """
    首页
    :param request:
    :return:
    """
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.select_related('category', 'author').all()[0:count]
    categories = NewsCategory.objects.all()
    context = {
        'newses': newses,
        'categories': categories,
        'banners': Banner.objects.all(),
    }
    return render(request, 'news/index.html', context=context)


def hot_news(request):
    news_hots = News.objects.all()
    return render(request, 'common/siderbar.html', {
        'news_hots': news_hots
    })

def news_list(request):
    """
    加载首页新闻
    通过p参数 指定获取第几页的数据
    :param request:
    :return:
    """
    page = int(request.GET.get('p', 1))
    category_id = int(request.GET.get('category_id', 0))
    start = int(page - 1) * settings.ONE_PAGE_NEWS_COUNT
    end = start + settings.ONE_PAGE_NEWS_COUNT
    if category_id == 0:
        newses = News.objects.select_related('category', 'author').all()[
                 start: end]
    else:
        newses = News.objects.select_related('category', 'author').filter(
            category_id=category_id)[start: end]
    serializer = NewsSerializer(newses, many=True)
    data = serializer.data
    return restful.result(data=data)


def news_detail(request, news_id):
    """
    新闻详情
    :param request:
    :param news_id:
    :return:
    """
    try:
        news = News.objects.select_related('category',
                                           'author').prefetch_related(
            'comments__author').get(pk=news_id)

        context = {
            'news': news
        }
        return render(request, 'news/news_detail.html', context=context)
    except News.DoesNotExist:
        raise Http404


@user_login_required
def public_comment(request):
    """
    发布评论
    :param request:
    :return:
    """
    form = PublicCommentForm(request.POST)
    if form.is_valid():
        news_id = form.cleaned_data.get('news_id')
        content = form.cleaned_data.get('content')
        news = News.objects.get(pk=news_id)
        comment = Comment.objects.create(content=content, news=news,
                                         author=request.user)
        serialize = CommentSerializer(comment)
        return restful.result(data=serialize.data)
    else:
        return restful.params_error(message=form.get_errors())


def search(request):
    return render(request, 'search/search.html')
