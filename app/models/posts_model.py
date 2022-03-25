from turtle import pu
import pymongo
from os import getenv
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client[getenv("DATABASE")]


class Post:
    def __init__(self, **kwargs) -> None:
        self.id = self.next_id()
        self.created_at = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
        self.updated_at = None
        self.title = kwargs["title"]
        self.author = kwargs["author"]
        self.tags = kwargs["tags"]
        self.content = kwargs["content"]

    @staticmethod
    def get_all_post():
        return db.posts.find()

    def create_post(self):
        db.posts.insert_one(self.__dict__)
        return self.__dict__

    @staticmethod
    def delete_post(id):
        return db.posts.find_one_and_delete({"id": id})

    @staticmethod
    def find_specif_post(id):
        return db.posts.find_one({"id": id})

    @classmethod
    def patch_post(self, id, payload):
        self.updated_at = self.patch_update_at()
        return db.posts.find_one_and_update(
            {"id": id},
            {
                "$set": {
                    **payload,
                    "updated_at": datetime.now().strftime("%d/%m/%Y %I:%M:%S %p"),
                }
            },
            return_document=pymongo.ReturnDocument.AFTER,
        )

    @classmethod
    def next_id(self):
        list_post = list(self.get_all_post())
        if len(list_post) > 0:
            return list_post[len(list_post) - 1]["id"] + 1
        return 1

    @classmethod
    def patch_update_at(self):
        return datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
