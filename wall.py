# wall.py

from pprint import pprint


def newsfeed(db, user):
    fol = db.users.find_one({"_id": user}, {"_id": 0, "followings": 1})['followings']
    fol.append(user)
    print("-" * 30, "[Newsfeed]", "-" * 30)
    cnt = db.posts.find({"writer_id": {'$in': fol}}).count()
    page = cnt // 5
    p = 0
    while p <= page:
        try:
            walls = list(db.posts.find({"writer_id": {'$in': fol}}).sort([("_id", -1)]).skip(p * 5).limit(5))
            for wall in walls:
                print("Post_num : ", wall["_id"], '\n',
                      "Date : ", wall["date"], '\n',
                      "WriterID : ", wall["writer_id"], '\n',
                      "WriterName : ", wall["writer_name"], '\n',
                      "Title : ", wall["title"], '\n',
                      "Text : ", wall["text"], '\n',
                      "Tags : ", wall["tags"], '\n',
                      "Comment : ", wall["comment"], '\n')
                print("=" * 50)
            if p == 0:
                print("This is the first page")
            if p == page:
                print("This is the last page")
            if p == page:
                np = input("previous page(a), next page(b), exit(c), insert_comment(i),delete_comment(d):")
                if np in ['a', 'A']:
                    if p == 0:
                        pass
                    else:
                        p -= 1
                elif np in ['c', 'C']:
                    return False
                elif np in ['i', 'I']:
                    text_num = int(input("Input post number to comment:"))
                    insertcomment(db, user, text_num)
                elif np in ['d', 'D']:
                    text_num = int(input("Input post number to delete comment:"))
                    deletecomment(db, user, text_num)
                else:
                    pass
            else:
                np = input("previous page(a), next page(b), exit(c), insert_comment(i),delete_comment(d):")
                if np in ['a', 'A']:
                    if p == 0:
                        pass
                    else:
                        p -= 1
                elif np in ['b', 'B']:
                    p += 1
                elif np in ['c', 'C']:
                    p = page + 1
                elif np in ['i', 'I']:
                    text_num = int(input("Input post number to comment:"))
                    insertcomment(db, user, text_num)
                elif np in ['d', 'D']:
                    text_num = int(input("Input post number to delete:"))
                    deletecomment(db, user, text_num)
                else:
                    pass
        except ValueError:
            print("The value you entered is invalid. Please try again.")


def insertcomment(db, user, text_num):
    try:
        if not db.posts.find({"_id": text_num}):
            raise NameError
        else:
            pass
        comm = input("Enter your comment:")
        db.posts.update_one({"_id": text_num}, {'$push': {'comment': {'commentor': user, 'text': comm}}})
    except NameError:
        print("The post is not exist!")
    except ValueError:
        print("The value you entered is invalid. Please try again.")


def deletecomment(db, user, text_num):
    try:
        if not db.posts.find({"_id": text_num}):
            raise NameError
        else:
            pass
        pprint(db.posts.find_one({"_id": text_num}))
        tex = input("Input comment to delete:")
        db.posts.update_one({"_id": text_num}, {'$pull': {'comment': {'commentor': user, 'text': tex}}})
    except NameError:
        print("The post is not exist!")
    except ValueError:
        print("The value you entered is invalid. Please try again.")


def getPosts(db, user):
    print("-" * 30, "[My wall]", "-" * 30)
    cnt = db.posts.find({"writer_id": user}).count()
    page = cnt // 5
    p = 0
    try:
        while p <= page:
            walls = list(db.posts.find({"writer_id": user}).hint([('writer_id', 1), ('_id', -1)]).skip(p * 5).limit(5))
            for my_wall in walls:
                print("Post_num : ", my_wall["_id"], '\n',
                      "Date : ", my_wall["date"], '\n',
                      "WriterID : ", my_wall["writer_id"], '\n',
                      "WriterName : ", my_wall["writer_name"], '\n',
                      "Title : ", my_wall["title"], '\n',
                      "Text : ", my_wall["text"], '\n',
                      "Tags : ", my_wall["tags"], '\n',
                      "Comment : ", my_wall["comment"], '\n')
                print("=" * 50)
            if p == 0:
                print("This is the first page")
            if p == page:
                print("This is the last page")
            if p == page:
                np = input("previous page(a), exit(c), insert_comment(i),delete_comment(d):")
                if np in ['a', 'A']:
                    if p == 0:
                        pass
                    else:
                        p -= 1
                elif np in ['c', 'c']:
                    return False
                elif np in ['i', 'I']:
                    text_num = int(input("Input post number to comment:"))
                    insertcomment(db, user, text_num)
                elif np in ['d', 'D']:
                    text_num = int(input("Input post number to delete:"))
                    deletecomment(db, user, text_num)
                else:
                    return False
            else:
                np = input("previous page(a), next page(b), exit(c), insert_comment(i),delete_comment(d):")
                if np in ['a', 'A']:
                    if p == 0:
                        pass
                    else:
                        p -= 1
                elif np in ['b', 'B']:
                    p += 1
                elif np in ['c', 'C']:
                    p = page + 1
                elif np in ['i', 'I']:
                    text_num = int(input("Input post number to comment:"))
                    insertcomment(db, user, text_num)
                elif np in ['d', 'D']:
                    text_num = int(input("Input post number to delete:"))
                    deletecomment(db, user, text_num)
                else:
                    pass
    except ValueError:
        print("The value you entered is invalid. Please try again.")
