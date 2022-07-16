import os
import mysql
from flask import Blueprint, render_template, request, redirect, jsonify
import requests



# about blueprint definition
assignment_4 = Blueprint('assignment_4', __name__
                         , static_folder='static',
                         template_folder='templates')


# ------------- DATABASE CONNECTION --------------- #
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host=os.getenv('DB_HOST'),
                                         user=os.getenv('DB_USER'),
                                         passwd=os.getenv('DB_PASSWORD'),
                                         database=os.getenv('DB_NAME'))
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    #

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ------------------- SELECT ---------------------- #

@assignment_4.route('/assignment_4')
def main():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list)


# -------------------- INSERT --------------------- #

@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    name = request.form['name']
    dog_name = request.form['dog_name']
    password = request.form['password']
    print(f'{name} {dog_name} {password}')
    query = "INSERT INTO users(name, dog_name, password) VALUES ('%s', '%s', '%s')" % (name, dog_name, password)
    interact_db(query=query, query_type='commit')
    return render_template('assignment_4.html', message='insert!')


# -------------------- DELETE --------------------- #

@assignment_4.route('/delete_user', methods=['get', 'POST'])
def delete_user_func():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query, query_type='commit')
    return render_template('assignment_4.html', message='delete!')


# -------------------- UPDATE --------------------- #

@assignment_4.route('/update_user', methods=['GET', 'POST'])
def update_user_func():
    name = request.form['name']
    dog_name = request.form['dog_name']
    password = request.form['password']
    id = request.form['id']
    query = "UPDATE users SET name ='%s',dog_name ='%s',password='%s'  WHERE id='%s';" % (name, dog_name, password, id)
    interact_db(query=query, query_type='commit')
    return render_template('assignment_4.html', message="changes made!")


@assignment_4.route('/other_update', methods=['GET', 'POST'])
def other_update():
    user_id = request.form['user_id']
    print(user_id)
    return render_template('up_date.html', id=user_id)




@assignment_4.route('/assignment_4/users', methods=['GET'])
def get_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    users_array = []
    for user in users_list:
        users_array.append({
            'dog_name': user.dog_name,
            'name': user.name
        })
    return jsonify(users_array)


@assignment_4.route('/assignment_4/outer_source', methods=['GET', 'POST'])
def outer_source():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    user_id = request.form['id']
    result = requests.get('https://reqres.in/api/users/' + user_id)
    return render_template('assignment_4.html', user_from_api=result.json()['data'],users=users_list)



@assignment_4.route('/assignment_4/restapi_users/', methods=['GET'])
def get_default_user():
    query = 'select * from users where id=13'
    user = interact_db(query, query_type='fetch')[0]
    user_dict = {
        'dogname' : user.dog_name,
        'name' : user.name
    }
    return jsonify(user_dict)



@assignment_4.route('/assignment_4/restapi_users/<int:USER_ID>', methods=['GET'])
def get_user(USER_ID):
    query = "select * from users where id='%s'" % USER_ID
    user = interact_db(query, query_type='fetch')[0]
    if user:
        user_dict = {
            'dogname': user.dog_name,
            'name': user.name
        }
        return jsonify(user_dict)
    return jsonify({
        'message': 'User not found. try again puppy'
    })