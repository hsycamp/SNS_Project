# follow.py


def follow(db, userid, following):
    try:
        if db.users.find_one({"_id": following}):
            if following in db.users.find_one({'_id': userid}, {'followings': 1, "_id": 0})['followings']:
                raise ValueError
            elif userid in db.users.find_one({'_id': following}, {'blacklist': 1, "_id": 0})['blacklist']:
                print("You have been blocked.")
            else:
                db.users.update_one({'_id': userid}, {'$push': {'followings': following}})
                db.users.update_one({'_id': following}, {'$push': {'followers': userid}})
                print("Follow completed.")
        else:
            print("The id is not exist.")
    except ValueError:
        print("You are already following.")


def unfollow(db, userid, following):
    try:
        if db.users.find_one({"_id": following}):
            if following not in db.users.find_one({'_id': userid}, {'followings': 1, "_id": 0})['followings']:
                raise ValueError
            else:
                db.users.update_one({'_id': userid}, {'$pull': {'followings': following}})
                db.users.update_one({'_id': following}, {'$pull': {'followers': userid}})
                print("Unfollow completed.")
        else:
            raise TypeError
    except ValueError:
        print("The id is not followed yet.")
    except TypeError:
        print("The id is not exist.")
    except:
        print("[Error]")


def blockInterface(db, user):
    username = db.users.find_one({"_id": user}, {"name": 1, "_id": 0})['name']
    try:
        print("=" * 25, "Blacklist", "=" * 25)
        print("\n1. block user_id\n"
              "2. unblock user_id\n"
              "3. go back")
        a = int(input("Choose one: "))

        if a == 1:
            block_list = db.users.find_one({"_id": user})["blacklist"]
            if block_list:
                print("Your blacklist : ", block_list)
            else:
                print("You have no id in blacklist.")
            black = input("Input user_id to block: ")
            if black == user:
                print("You can't block yourself!")
            else:
                block(db, user, black)
        elif a == 2:
            block_list = db.users.find_one({"_id": user})["blacklist"]
            if block_list:
                print("Your blacklist : ", block_list)
            else:
                print("You have no id in blacklist.")
            black = input("Input user_id to unblock: ")
            if black == user:
                print("You can't unblock yourself!")
            else:
                unblock(db, user, black)
        elif a == 3:
            print("\n\n")
            pass
        else:
            print("Invalid input! You must type a number between 1 and 3")
    except ValueError:
        print('The value you entered is invalid. Please try again.')


def block(db, user, black):
    try:
        if db.users.find_one({"_id": black}):
            if black in db.users.find_one({'_id': user}, {'blacklist': 1, "_id": 0})['blacklist']:
                raise ValueError
            else:
                db.users.update_one({'_id': user}, {'$push': {'blacklist': black}})
                print("Blocking completed.")
                unfollow(db, black, user)
        else:
            print("The id is not exist.")
    except ValueError:
        print("You are already blocked.")


def unblock(db, user, black):
    try:
        if db.users.find_one({"_id": black}):
            if black not in db.users.find_one({'_id': user}, {'blacklist': 1, "_id": 0})['blacklist']:
                raise ValueError
            else:
                db.users.update_one({'_id': user}, {'$pull': {'blacklist': black}})
                print("Unblocking completed.")
        else:
            raise TypeError
    except ValueError:
        print("The id is not blocked.")
    except TypeError:
        print("The id is not exist.")
    except:
        print("[Error]")
