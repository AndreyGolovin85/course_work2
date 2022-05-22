import json


def overwrite_json_files(path, list):
    """
    Функция записывает пост в закладки
    :param list: list
    :return:
    """
    with open(path, "w",  encoding="utf-8") as file:
        json.dump(list, file, ensure_ascii=False)


def get_posts_all(path) -> list:
    """
    Функция возвращает список всех постов.
    :return: list
    """
    with open(path, "r", encoding="utf-8") as all_post:
        return json.load(all_post)


def get_posts_by_user(path, user_name) -> list:
    """
    Функция возвращает посты определенного пользователя.
    :param user_name: str
    :return: list
    """
    all_posts = get_posts_all(path)
    user_posts = []
    for post in all_posts:
        if post["poster_name"].lower() == user_name.lower():
            user_posts.append(post)
    return user_posts


def get_comments_by_post_id(path, post_id) -> list:
    """
    возвращает комментарии определенного поста
    :param post_id: int
    :return: list
    """
    with open(path, "r", encoding="utf-8") as file:
        all_comments = json.load(file)
    list_comments_by_id = []
    for comment in all_comments:
        if comment["post_id"] == post_id:
            list_comments_by_id.append(comment)
    return list_comments_by_id


def search_for_posts(path, query) -> list:
    """
    возвращает список постов по ключевому слову
    :param query: str
    :return: list
    """
    all_post = get_posts_all(path)
    found_list_post = []
    for post in all_post:
        if query.lower() in post["content"].lower() and len(found_list_post) <= 10:
            found_list_post.append(post)
    return found_list_post


def get_post_by_pk(path, pk) -> dict:
    """
    возвращает один пост по его идентификатору
    :param pk: int
    :return: dict
    """
    all_post = get_posts_all(path)
    for pk_post in all_post:
        if pk_post["pk"] == pk:
            return pk_post


"""
def get_post_by_tag(pk) -> str:
    post = get_post_by_pk(pk)
    print(1, post)
    list_word = post["content"]
    index = list_word.find("#")
    return index
"""
