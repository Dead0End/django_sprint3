from blog.models import Post, Category
from constants import date_now


def get_posts():
    """Вернуть результат запроса к таблице blog_post."""
    query_set = (
        Post.objects.select_related(
            "category",
            "location",
            "author",
        )
        .filter(
            pub_date__lte=date_now,
            is_published=True,
            category__is_published=True,
        )
    )
    return query_set


def get_category():
    """Вернуть результат запроса к таблице blog_category."""
    query_set = Category.objects.filter(
        is_published=True
    )
    return query_set
