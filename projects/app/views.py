from datetime import datetime

from app import settings
from app.dao import user_create
from app.errors import BadRequestError
from app.http import Response
from app.model import User
from app.settings import generate_id
from validators import check_validators
import settings
import dao


def user_create_pro(user: User):
    try:
        check_validators(user)
        user.user_id = str(generate_id())
        user.created_at = str(datetime.now())
        user.password = str(settings.encode_password(user.password))
        user_create(user)
        return Response('User successfully created')
    except BadRequestError as e:
        return Response('Bad requests', status_code=404)


def update_user_pro():
    user_id = input('Enter user id: ')
    updated_user = dao.user_update(user_id)
    if updated_user:
        response = Response('User Successfully updated')
        if response.message:
            # sms sending
            print(response.message, response.status_code)


def delete_user_pro():
    user_id = input('Enter user id: ')
    is_user_deleted = dao.user_delete(user_id)
    if not is_user_deleted:
        raise BadRequestError('User id not found in my db')
    else:
        response = Response('User successfully deleted')
        if response.message:
            print(response.message, response.status_code)


