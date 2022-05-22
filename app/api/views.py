from flask import Blueprint, jsonify, request
from utils import get_posts_all, get_post_by_pk

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/api/posts/")
def posts_all():
    return jsonify(get_posts_all())


@api_blueprint.route("/api/post/<int:post_id>")
def one_post(post_id):
    return jsonify(get_post_by_pk(post_id))
