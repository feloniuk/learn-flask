from flask import Flask, request

app = Flask(__name__)  # создаем объект app на основе класса Flask, (__name__) - имя нашего файла

# use Python Dict as DB
storage = dict()
# structure of storage: key - username, value - dict(default empty) in future will contain info about current user


# put some default users into db
storage.update(
    {
        "username1": {},
        "username2": {}
    }
)


@app.route('/')  # отслеживает URL ('/') - main page)
def hello_world():
    return 'Hello, World!'


@app.route('/users/list/')
def user_list():
    username_list = storage.keys()
    return '<br>'.join(username_list)



@app.route('/users/delete/<username>')
def delete_user(username):
    old_users = storage.copy()
    storage.pop(username, False)
    if username in old_users:
        return 'User  was deleted'
    else:
        return 'User doesn`t exist or already deleted'



@app.route('/users/add/<username>')
def add_user_list(username):
    new_users = storage.copy()
    storage.update({username:{}})
    if username in new_users:
        return f'User {username} already in list'
    else:
         return f'User {username} added'


@app.route('/user/add/<usernames>', methods=['POST'])
def add_user_list2(usernames):
    username = request.form.get('usernames')
    new_users = storage.copy()
    storage.update({username:{}})
    if username in new_users:
        return f'User {username} already in list'
    else:
         return f'User {username} added'

if __name__=='__main__': # если запускается через файл app.py, то проект должен запуститься как flask приложение
    app.run(debug=True)   # запускается локальный сервер
