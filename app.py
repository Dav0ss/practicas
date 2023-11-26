from flask import Flask, render_template, session, request, redirect, url_for, flash

app = Flask(__name__)

# palabra clave
app.secret_key = 'yopuedohacerlotambien'


@app.route('/')
def index():
    if 'usuario' in session:
        return render_template('base.html')
    else:
        return redirect(url_for('login'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET' :
        return render_template('login.html')
    else:
        print(request.form)
        usuario = request.form['usuario']
        clave = request.form['clave']
        if usuario == 'david' and clave == '123':
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:         
            return redirect(url_for('login'))
