from flask import Flask, abort, jsonify, make_response, request

from decorators import auth
from model import db, User, user_schema, users_schema


app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.errorhandler(404)
def not_found(error):
    """ возвразает ответ с кодом ошибки 404 в формате .json при отсутствии данных"""
    return make_response(jsonify({'error': 'data not found'}), 404)


@app.route('/users', methods=['GET'])
@auth.login_required
def get_all_users():
    """ возвращает список всех пользователей в формате .json """
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify({'users': result})

@app.route('/users/<int:id>', methods=['GET'])
@auth.login_required
def get_the_user(id):
    """ возвращает данные пользователя по полученному ID"""
    if User.query.get(id):
        user = User.query.get(id)
        result = user_schema.dump(user)
        return jsonify({'user': result})
    abort(404)

@app.route('/users', methods=['POST'])
@auth.login_required
def add_user():
    """ добавляет нового пользователя в базу """
    if not request.json or not 'user_name' in request.json:
        abort(400)
    user_exists = User.query.filter(User.user_name == request.json['user_name']).count()
    if not user_exists:
        user_name = request.json['user_name']
        country = request.json['country']
        new_user = User(user_name, country)
        # добавляем пользователя в базу
        db.session.add(new_user)
        db.session.commit()

        new_user = user_schema.dump(new_user)
        return jsonify({'user': new_user}), 201
    else:
        return jsonify({'error': 'user exists'}), 409

@app.route('/users/<int:id>', methods=['PUT'])
@auth.login_required
def update_user(id):
    """ обновляет данные пользователя """
    current_user = User.query.get(id)
    if not current_user:
        abort(404)
    if not request.json:
        abort(400)
    current_user.user_name = request.json['user_name']
    current_user.country = request.json['country']

    db.session.commit()

    current_user = user_schema.dump(current_user)
    return jsonify({'user': current_user})

@app.route('/users/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_user(id):
    """ удаляет пользователя """
    current_user = User.query.get(id)
    db.session.delete(current_user)
    db.session.commit()
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)
