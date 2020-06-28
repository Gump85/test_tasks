# Simple REST API
Простое приложение на Python + фреймворк Flask + SQLAlchemy, представляющая собой 
REST API по работе с сущностью User
Для защиты приложениея используется basic access authentication со следующими парамерами
пользователя:
Логин: benz
Пароль: motorwagen

## Запуск приложения
MacOS и Linux
```
python3 app.py
```

## Возможности REST API
для тестирования запросов используется утилита curl

1. Получение списка всех пользователей
```
curl -u benz:motorwagen -i http://localhost:5000/users
```
2. Получение данных по одному пользователю по id (в URI id необходимо указать целое число
начиная с 1)
```
curl -u benz:motorwagen -i http://localhost:5000/users/id
```
3. Редактировать данные пользователя по id:(для изменения данных необходимо запольнить словарь
{"field":"new_data",...})
```
curl -u benz:motorwagen -i -H "Content-Type: application/json" -X PUT -d '{"field":"new_data,..."}' http://localhost:5000/users/id
```
4. Добавление пользователя в базу
```
curl -u benz:motorwagen -i -H "Content-Type: application/json" -X POST -d '{"field":"new_data,..."}' http://localhost:5000/users/
```
5. удаление пользователя по id (в URI id необходимо указать целое число
начиная с 1)
```
curl -u benz:motorwagen -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/users/id
```
