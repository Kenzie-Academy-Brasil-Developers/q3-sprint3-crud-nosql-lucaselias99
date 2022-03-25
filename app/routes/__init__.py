from flask import Flask
from app.routes.posts_route import posts_route


def init_app(app: Flask):
    posts_route(app)
