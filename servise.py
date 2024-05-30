from db import cur, conn
from models import User
from sessions import Session
import utils

session = Session()


def login(username: str, password: str):
    user: Session | None = session.check_session()
    if user:
        return utils.BadRequest('You are already logged in', status_code=401)

    get_user_by_username_query = '''SELECT * FROM users WHERE username = %s;'''
    cur.execute(get_user_by_username_query, (username,))
    user_data = cur.fetchone()

    if not user_data:
        return utils.BadRequest('Username not found in the database')

    _user = User(username=user_data[1], password=user_data[2], role=user_data[3], status=user_data[4],
                 login_try_count=user_data[5])

    if password != _user.password:
        update_count_query = """UPDATE users SET login_try_count = login_try_count + 1 WHERE username = %s;"""
        cur.execute(update_count_query, (_user.username,))
        conn.commit()

    user.add_session(_user)
    return utils.ResponseData('User successfully logged in')


def login_project(username, password):
    if username == "admin" and password == "12345":
        print("Login successful. Welcome to the project!")
    else:
        print("Login failed. Please check your credentials.")


login_project("admin", "12345")
login_project("user", "password123")
login_project("guest", "pass123")

while True:
    choice = input('Enter your choice: ')
    if choice == '1':
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        login(username, password)
    else:
        break