from app import db, app

# создаем базу данных
db.create_all(app=app)
