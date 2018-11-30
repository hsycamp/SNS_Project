# user.py

from follow import *
from post import *
from wall import *


def signup(db):
    # id_input
    try:
        id = input("id: ")
        if id == "":
            print("A length of id should be at least 1")
            return False
        if db.users.find_one({"_id": id}):
            raise NameError
            # Check if the id already exists.
        pw = input("password: ")
        if pw == "":
            print("A length of password should be at least 1")
            return False
        else:
            pw1 = input("input password again:")
            if pw != pw1:
                print("Wrong password! try again!")
                raise ValueError
            name = input("name: ")
            if name == "":
                raise ValueError
            db.users.insert_one(
                {"_id": id, "password": pw, "name": name, "status_message": [], "followings": [], "followers": [],
                 "blacklist": []})
            return
    except NameError:
        print("The user id already exists. Please try again with another!\n")
        print()
    except:
        print('The value you entered is invalid. Please try again.\n')
        print()
        signup(db)


def signin(db):
    try:
        print("-------------[login]--------------")
        id = input("ID: ")
        if id == "":
            print("A length of id should be at least 1")
            return False
        if not db.users.find_one({"_id": id}):
            print("not exist!\n")
            raise ValueError
        pw = input("password:")
        if not db.users.find_one({"_id": id, "password": pw}):
            print("Wrong Password! try again!\n")
            raise ValueError
        print("Welcome!\n")
        userpage(db, id)
    except:
        print('The value you entered is invalid. Please try again.\n')
        signin(db)


def mystatus(db, user):
    followers = db.users.find_one({"_id": user}, {"followers": 1, "_id": 0})['followers']
    followings = db.users.find_one({"_id": user}, {"followings": 1, "_id": 0})['followings']
    status_message = db.users.find_one({"_id": user}, {"status_message": 1, "_id": 0})['status_message']
    try:
        print("=*=" * 15)
        print("Profile: \n Status_message: {0} \n Followers: {1} \n Followings: {2}".
              format(status_message, len(followers), len(followings)))
        print("=*=" * 15)
        print("-" * 30)
        print("1. Edit my status message\n"
              "2. Show my followers\n"
              "3. Show my followings\n"
              "4. Go back")
        print("-" * 30)
        b = int(input('Choose one : '))
        if b == 1:
            c = input("Input to status message:")
            if c == "":
                print("Input at least 1 letter.")
            else:
                d = input("Are you sure?(y/n):")
                if d in ['y', 'Y']:
                    db.users.update_one({'_id': user}, {'$set': {'status_message': c}})
                    print("Completed.")
                    mystatus(db, user)
                elif d in ['n', 'N']:
                    mystatus(db, user)
                else:
                    print("Wrong input!")
        elif b == 2:
            if followers:
                print("follower list:\n", followers)
            else:
                print("You have no followers.")
            input("If you want to go back, press enter key.")
            mystatus(db, user)
        elif b == 3:
            if followings:
                print("following list:\n", followings)
            else:
                print("You have no followings.")
            input("If you want to go back, press enter key.")
            mystatus(db, user)
        elif b == 4:
            pass
        else:
            print("Wrong input!")
            mystatus(db, user)
    except ValueError:
        print('The value you entered is invalid. Please try again.\n')


def userpage(db, user):
    while True:
        try:
            print("-----[Welcome FIRA!!]-----\n"
                  "1. My status\n"
                  "2. News feed\n"
                  "3. Wall\n"
                  "4. Post\n"
                  "5. Follow\n"
                  "6. Unfollow\n"
                  "7. #Searching\n"
                  "8. blacklist\n"
                  "9. Logout\n")
            b = int(input("\nChoose one:"))
            if b == 1:
                mystatus(db, user)
            elif b == 2:
                newsfeed(db, user)
            elif b == 3:
                getPosts(db, user)
            elif b == 4:
                postInterface(db, user)
            elif b == 5:
                following_list = db.users.find_one({"_id": user})["followings"]
                if following_list:
                    print("Your followings : ", following_list)
                else:
                    print("You have no followings")
                following = input("Input user_id to follow:")
                if following == user:
                    print("You can't follow yourself!")
                else:
                    follow(db, user, following)
            elif b == 6:
                following_list = db.users.find_one({"_id": user})["followings"]
                if following_list:
                    print("Your followings : ", following_list)
                else:
                    print("You have no followings")
                following = input("Input user_id to unfollow:")
                unfollow(db, user, following)
            elif b == 7:
                findTag(db, user)

            elif b == 8:
                blockInterface(db, user)
            elif b == 9:
                return
            else:
                print("Wrong input!\n")
        except ValueError:
            print('The value you entered is invalid. Please try again.\n')
