import json
from pprint import pprint

from app.errors import BadRequestError
from app.model import User


def user_read(user_id: str):
    with open('db/users.json', 'r') as f:
        users = json.load(f)
        return users[user_id]


def user_lists():
    with open('db/users.json', 'r') as f:
        users = json.load(f)
        return users


def user_create(user: User):
    with open('db/users.json', 'r+') as file:
        users = json.load(file)
        users[user.user_id] = user.__dict__
        file.seek(0)
        json.dump(users, file, indent=4)


# user = User(full_name='Tolmas Abdujalilov', password='admin345', user_id='2222')


def user_update(new_id: str):
    users = user_lists()
    for user_id, data in users.items():
        if user_id == new_id:
            data["full_name"] = input("Enter your full name: ")
            data["email"] = input("Enter your email : ")
            with open("db/users.json", 'w') as f:
                json.dump(users, f, indent=3)
            return True
    else:
        raise BadRequestError(f'User id not found')


def user_delete(new_id: str):
    users = user_lists()
    # users[new_id] = None
    if new_id in users:
        users.pop(new_id)
        with open('db/users.json', 'w') as f:
            json.dump(users, f, indent=3)
        return True

    else:
        return False

