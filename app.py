from flask import Flask, render_template, session, request, redirect, url_for, flash
from referencial.ciudad.ciudadDAO import CiudadDAO

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

#carga la vista de tabla en la opcion registrar cuenta

@app.route('/vista-tabla-registrar-cuenta')
def vistaTabla():
    return render_template('tabla1.html')

@app.route('/index-ciudad')
def index_ciudad():
    cdao = CiudadDAO()
    lista = cdao.getCiudades()
    diccionario = []
    if len(lista) > 0:
        for item in lista:
            diccionario.append(
                {
                    'id_ciudad': item[0],
                    'descri_ciudad': item[1]
                }
            )
    return render_template('vista_ciudades/index_ciudades.html', ciudad=diccionario)

@app.route('/index-persona')
def index_persona():
    return render_template('vista_persona/index_persona.html')