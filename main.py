# main.py

from pymongo import MongoClient
from user import *

client = MongoClient()
db = client.sns_project


def mainpage(db):
    print("\n\n\n\n\n[[**---Wellcome to Mongo SNS---**]]\n"
          "\n--------[ Menu ]--------\n"
          "\n1.Sign up\n"
          "2.Sign in\n"
          "3.Exit\n")
    try:
        sign = int(input("\nChoose one:"))
        if sign == 1:
            signup(db)
        elif sign == 2:
            signin(db)
        elif sign == 3:
            exit()
        else:
            print("Invalid input! You must type a number between 1 and 3.\n")
    except ValueError:
        print('The value you entered is invalid. Please try again.\n')
    mainpage(db)


if __name__ == "__main__":
    if not list(db.users.find()):
        db.users.insert_one(
            {"_id": 'root', "password": 'root', "name": 'root', "status_message": [], "followings": [],
             "followers": []})
    if not list(db.posts.find()):
        db.posts.insert_one(
            {"_id": 0, "title": 'Notice', "text": 'text_for_index', "date": '2000-10-12 22:16:10', "writer_id": 'root',
             "writer_name": 'root', "tags": [],
             "comment": []})
        db.posts.create_index([("writer_id", 1), ("_id", -1)])
    mainpage(db)
