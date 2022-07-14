from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from datetime import timedelta
import mysql.connector

app = Flask(__name__)


app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


@app.route('/')
def index_func():
    return redirect(url_for('Home_page'))


@app.route('/homepage')
def Home_page():
    return render_template('homepage.html')


@app.route('/contactus')
def contactus_page():
    return render_template('contactus.html')

@app.route('/assignment3_1')
def assignment3_1():
    db_username = 'Lover'
    dog_names = ('bobo', 'tedy', 'haim')
    dog_types = ('golden retriever', 'shitzu', 'aski')
    hobbies = ('drawing', 'books', 'ships', 'chips', 'TV', 'sea')
    return render_template('assignment3_1.html', dog_names=dog_names, dog_types=dog_types,
                           hobbies=hobbies, username=db_username)



users = {
    "1": {"name": "gal", "dog_name": "papa"},
    "2": {"name": "ran", "dog_name": "gig"},
    "3": {"name": "or", "dog_name": "sisi"},
    "4": {"name": "ron", "dog_name": "coco"},
    "5": {"name": "reef", "dog_name": "lir"}

}
user_dict = {
    'gal': '1111',
    'ran': '2222',
    'or': '3333',
    'ron': '4444',
    'reef': '5555',
}


@app.route('/assignment3_2', methods=['GET', 'POST'])
def assignment3_2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in user_dict:
            pas_in_dict = user_dict[username]
            if pas_in_dict == password:
                session['username'] = username
                session['logedin'] = True
                return render_template('assignment3_2.html',
                                       message='Success',
                                       username=username)
            else:
                return render_template('assignment3_2.html',
                                       message='Wrong password!')
        else:
            return render_template('assignment3_2.html',
                                   message='Please sign in!')

    if 'name' in request.args:
        name = request.args["name"]
        if name == '':
            return render_template('assignment3_2.html', users=users)
        c_dogName = None
        for dog_name in users.values():
            if dog_name['name'] == name:
                c_dogName = dog_name
                break
        if c_dogName:
            return render_template('assignment3_2.html',
                                   name=c_dogName['name'],
                                   dog_name=c_dogName['dog_name'])
        else:
            return render_template('assignment3_2.html',
                                   message2='HI love, Try another name')
    return render_template('assignment3_2.html',
                           users=users)


@app.route('/log_out')
def logout_func():
    session['logedin'] = False
    session.clear()
    return redirect(url_for('assignment3_2'))


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))


#--------4-------------#
from pages.assignment_4.assignment_4 import assignment_4
app.register_blueprint(assignment_4)





if __name__ == '__main__':
    app.run(debug=True)
