from flask import Flask, request
from app.controllers import post_controller


def posts_route(app: Flask):
    @app.post("/posts")
    def create_post():
        return post_controller.create_post_controller()

    @app.delete("/posts/<int:id>")
    def delete_post(id):
        return post_controller.delete_post_controller(id)

    @app.get("/posts/<int:id>")
    def read_post_by_id(id):
        return post_controller.read_post_by_id_controller(id)

    @app.get("/posts")
    def read_posts():
        return post_controller.read_posts_controller()

    @app.patch("/posts/<int:id>")
    def update_post(id):
        return post_controller.update_post_controller(id)
