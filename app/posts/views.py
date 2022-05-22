from flask import Blueprint, request, render_template, redirect

import setting

from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_posts_by_user, search_for_posts, \
    overwrite_json_files

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")


@posts_blueprint.route("/")
def posts_all():
    """
    Блюепринт выводит все посты
    :return: html
    """
    try:
        all_posts = get_posts_all(setting.POSTS)
        return render_template("index.html", all_posts=all_posts)
    except:
        return "Что-то пошло не так!"


@posts_blueprint.route("/posts/<int:post_id>")
def one_post(post_id):
    """
    Блюепринт выводит информацию одного поста
    :param post_id: int
    :return: html
    """
    try:
        one_post = get_post_by_pk(setting.POSTS, post_id)
        post_comments = get_comments_by_post_id(setting.COMMENTS, post_id)
    except:
        return "Ошибка поста"
    else:
        if one_post is None:
            return "Такой пост не найден", 404
    return render_template("post.html", one_post=one_post, post_comments=post_comments,
                            count_comment=len(post_comments))


@posts_blueprint.route("/search", methods=["GET"])
def search_post():
    """
    Блюепринт выводит посты с ключевым словом
    :return: html
    """
    try:
        s = request.args.get("s")
        search_posts = search_for_posts(setting.POSTS, s)
        return render_template("search.html", search_posts=search_posts, count_post=len(search_posts))
    except:
        return "Ошибка поиска"


@posts_blueprint.route("/user/<username>")
def search_posts_user(username):
    """
    Поиск по имени
    :param username: str
    :return: html
    """
    user_posts = get_posts_by_user(setting.POSTS, username)
    return render_template("user-feed.html", user_posts=user_posts)


@posts_blueprint.route("/bookmarks")
def bookmarks_posts():
    """
    Вывод постов добавленых в закладки
    :return:
    """
    bookmarks = get_posts_all(setting.BOOKMARKS)
    count_bookmark = len(bookmarks)
    if count_bookmark > 0:
        return render_template("bookmarks.html", bookmarks=bookmarks,
                               count_bookmark=count_bookmark)                   # count_bookmark
    else:                                                                       # Не выводит количество
        return "Нет постов для отображения"                                     # постов в закладках


@posts_blueprint.route("/bookmarks/add/<int:post_id>")
def bookmarks_add_posts(post_id):
    """
    Добавляем пост в закладки
    :param post_id: int
    :return:
    """
    post = get_post_by_pk(setting.POSTS, post_id)
    bookmarks = get_posts_all(setting.BOOKMARKS)
    bookmarks.append(post)
    """
    for post_bookmarks in bookmarks:
        if post_id != post_bookmarks["pk"]:
            bookmarks.append(post)
        else:
            print(type(post_bookmarks["pk"]))
            return "Такой пост уже есть в закладках"
    """
    overwrite_json_files(setting.BOOKMARKS, bookmarks)
    return redirect("/", code=302)


@posts_blueprint.route("/bookmarks/remove/<int:post_id>")
def bookmarks_remove_posts(post_id):
    """
    Удаляем пост из закладок
    :param post_id:
    :return:
    """
    bookmarks = get_posts_all(setting.BOOKMARKS)
    for bookmark in bookmarks:
        if bookmark["pk"] == post_id:
            bookmarks.remove(bookmark)
    overwrite_json_files(setting.BOOKMARKS, bookmarks)

    return redirect("/", code=302)


