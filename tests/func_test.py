import pytest

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_posts_by_user, search_for_posts


def test_post_all():
    all_posts = get_posts_all()
    assert type(all_posts) == list, "Список постов должен быть списком"
    assert type(all_posts[0]) == dict, "Один пост должен быть словарь"


def test_post_all_key():
    all_posts = get_posts_all()
    first_post = all_posts[0]
    keys_expected = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
    first_post_key = set(first_post.keys())
    assert first_post_key == keys_expected, "Полученные ключи не равны"


id_post_parametrs = [1, 2, 3, 4, 5, 6, 7, 8]

@pytest.mark.parametrize("id_post", id_post_parametrs)
def test_post_by_pk(id_post):
    one_post = get_post_by_pk(id_post)
    assert type(id_post) == int, "Идентификатор поста должен быть целое число"
    assert type(one_post) == dict, "Пост должен быть словарь"


def test_comments_by_post_id():
    id_post = 3
    list_comment = get_comments_by_post_id(id_post)
    assert type(id_post) == int, "Идентификатор поста должен быть целое число"
    assert type(list_comment) == list, "Список комментариев должен быть списком"
    assert type(list_comment[0]) == dict, "Один комментарий должен быть словарь"


def test_get_posts_by_user():
    search_posts_user = "johnny"
    list_user = get_posts_by_user(search_posts_user)
    assert type(search_posts_user) == str, "Значение поиска по постам должно быть строка"
    assert type(list_user) == list, "Список постов должен быть списком"
    assert type(list_user[0]) == dict, "Один пост должен быть словарь"


def test_search_for_posts():
    search_posts = "незаметно"
    list_posts = search_for_posts(search_posts)
    assert type(search_posts) == str, "Значение поиска по постам должно быть строка"
    assert type(list_posts) == list, "Список постов должен быть списком"
    assert type(list_posts[0]) == dict, "Один пост должен быть словарь"
