from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):
    """ сущноть пользователь """
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    country = db.Column(db.String(200))

    def __init__(self, user_name, country):
        """ инициализация нового пользователя """
        self.user_name = user_name
        self.country = country

    def __repr__(self):
        """ формат отображения при запросе """
        return f'User_name {self.user_name}'

class UserSchima(ma.Schema):
    """ опредялем формат вывода данных """
    class Meta:
        fields = ('id', 'user_name', 'country')

user_schema = UserSchima()
users_schema = UserSchima(many=True)
