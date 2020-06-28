from flask import jsonify, make_response
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    """ возвращает по имени пользователя пароль """
    if username == 'benz':
        return 'motorwagen'


@auth.error_handler
def unauthorized():
    """ отправляет ошибку авторизации """
    return make_response(jsonify({'error': 'Unauthorized acsess'}), 403)
