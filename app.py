from flask import Flask, render_template, session, request, redirect, url_for
from referencial.ciudad.ciudadDAO import CiudadDAO


app = Flask(__name__)
app.secret_key = 'yopuedohacerlotambien'

@app.route('/init')
def hola():
    return 'hola'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'you are not logged in'
   
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form method="post">
        <p><input type=text name=username>
        <p><input type=submit value=Login>
    </form>
    '''