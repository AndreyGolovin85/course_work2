import tests

from app.api.views import posts_all, one_post


def post_all_type():
    posts = posts_all()
    assert type(posts) == list, "Список постов должен быть списком"
    assert type(posts[0]) == dict, "Один пост должен быть словарь"


#def
