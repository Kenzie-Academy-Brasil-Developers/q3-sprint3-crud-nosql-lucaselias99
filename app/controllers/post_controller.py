from app.models.posts_model import Post
from http import HTTPStatus
from flask import request, jsonify


def read_posts_controller():
    posts = list(Post.get_all_post())
    for post in posts:
        del post["_id"]
    return jsonify(posts), HTTPStatus.OK


def create_post_controller():
    data = request.get_json()
    try:
        post = Post(**data)
    except KeyError:
        return {"error": "Erro de chave"}, HTTPStatus.BAD_REQUEST
    post = post.create_post()
    del post["_id"]
    return jsonify(post), HTTPStatus.CREATED


def read_post_by_id_controller(id):
    try:
        post = Post.find_specif_post(id)
        del post["_id"]
        return jsonify(post), HTTPStatus.OK
    except:
        return {"msg": "Post não encontrado"}, HTTPStatus.NOT_FOUND


def update_post_controller(id):
    try:
        data = request.get_json()
        post = Post.patch_post(id, data)
        del post["_id"]
        return jsonify(post), HTTPStatus.OK
    except:
        return {"msg": "Post não encontrado"}, HTTPStatus.NOT_FOUND


def delete_post_controller(id):
    try:
        post = Post.delete_post(id)
        del post["_id"]
        return jsonify(post), HTTPStatus.OK
    except:
        return {"msg": "Post não encontrado"}, HTTPStatus.NOT_FOUND
