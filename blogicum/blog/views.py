from django.shortcuts import render, get_object_or_404

from core.same_requests import get_posts, get_category

from constants import MAX_RES_CATEGORY_POSTS
from constants import MAX_RES_INDEX


def index(request):
    """Главная страница, Лента записей"""
    post_list = get_posts().order_by("-pub_date")
    [:MAX_RES_INDEX].prefetch_related('category')
    context = {"post_list": post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """Подробное описание выбранной записи"""
    post = get_object_or_404(get_posts().prefetch_related('category'), pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Отображение публикации по категории"""
    category = get_object_or_404(get_category(), slug=category_slug)
    post_list = get_posts().filter(category=category).order_by(
        "-pub_date")[:MAX_RES_CATEGORY_POSTS]
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
