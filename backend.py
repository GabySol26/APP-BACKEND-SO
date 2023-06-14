from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL #pip install flask-mysql
import pymysql

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'Gaby'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tf123@'
app.config['MYSQL_DATABASE_DB'] = 'TF'
app.config['MYSQL_DATABASE_HOST'] = '3.95.151.155' #no olvidar cambiar la ip
mysql.init_app(app)

#enable CORS
CORS(app, resources={r'/*': {'origins': ''}})

# sanity check route
@app.route('/')
def home():
    tabla = request.args.get('tabla', 'Paciente')
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM {}".format(tabla))
        data = cursor.fetchall()
        return jsonify({
            'status': 'success',
            'data': data,
            'tabla': tabla
        })
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# GET'S ALL

@app.route('/pacientes', methods=['GET'])
def pacientes():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Paciente order by idPaciente")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Pacientes': data
    })

@app.route('/medicos', methods=['GET'])
def medicos():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Medico order by idMedico")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Medicos': data
    })

@app.route('/citas', methods=['GET'])
def citas():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Cita order by idCita")
    data = cursor.fetchall()
    for row in data: 
        row['hora'] = str(row['hora'])
    return jsonify({
        'status': 'success',
        'Citas': data
    })

@app.route('/tratamientos', methods=['GET'])
def tratamientos():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM Tratamiento order by idTratamiento")
    data = cursor.fetchall()
    return jsonify({
        'status': 'success',
        'Tratamientos': data
    })

#GET'S BY ID

@app.route('/paciente/<string:id>', methods=['GET', 'POST'])
def paciente_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Paciente WHERE idPaciente = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'paciente' + id : row
    })

@app.route('/medico/<string:id>', methods=['GET', 'POST'])
def medico_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Medico WHERE idMedico = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'medico' + id: row
    })        

@app.route('/cita/<string:id>', methods=['GET', 'POST'])    
def cita_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Cita WHERE idCita = %s", [id])
    row = cursor.fetchone()
    row['hora'] = str(row['hora'])

    return jsonify({
        'status': 'success',
        'cita' + id: row
    })

@app.route('/tratamiento/<string:id>', methods=['GET', 'POST'])
def tratamiento_id(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(id)
    cursor.execute("SELECT * FROM Tratamiento WHERE idTratamiento = %s", [id])
    row = cursor.fetchone()

    return jsonify({
        'status': 'success',
        'tratamiento' + id: row
    })

# POST'S 

@app.route('/paciente', methods=['GET', 'POST'])
def paciente():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        nombre = post_data.get('nombre')
        apellidop = post_data.get('apellidop')
        apellidom = post_data.get('apellidom')
        dni = post_data.get('dni')
        genero = post_data.get('genero')
        fnac = post_data.get('fnac')
        email = post_data.get('email')
        telef = post_data.get('telef')

        print(nombre)
        print(apellidop)
        print(apellidom)
        print(dni)
        print(genero)
        print(fnac)
        print(email)
        print(telef)

        sql = "INSERT INTO Paciente (nombre, apellidop, apellidom, dni, genero, fnac, email, telef) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (nombre, apellidop, apellidom, dni, genero, fnac, email, telef)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Paciente agregado!'
    return jsonify(response_object)

@app.route('/medico', methods=['GET', 'POST'])
def medico():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        nombreM = post_data.get('nombreM')
        apellidoPM = post_data.get('apellidoPM')
        apellidoMM = post_data.get('apellidoMM')
        dniM = post_data.get('dniM')
        generoM = post_data.get('generoM')
        emailM = post_data.get('emailM')
        fnacimientoM = post_data.get('fnacimientoM')
        numColegialM = post_data.get('numColegialM')
        especialidad = post_data.get('especialidad')

        print(nombreM)
        print(apellidoPM)
        print(apellidoMM)
        print(dniM)
        print(generoM)
        print(emailM)
        print(fnacimientoM)
        print(numColegialM)
        print(especialidad)

        sql = "INSERT INTO Medico (nombreM, apellidoPM, apellidoMM, dniM, generoM, emailM, fnacimientoM, numColegialM, especialidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (nombreM, apellidoPM, apellidoMM, dniM, generoM, emailM, fnacimientoM, numColegialM, especialidad)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Medico agregado!'
    return jsonify(response_object)

@app.route('/cita', methods=['GET', 'POST'])
def cita():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        fecha = post_data.get('fecha')
        hora = post_data.get('hora')
        nota = post_data.get('nota')
        idPaciente = post_data.get('idPaciente')
        idMedico = post_data.get('idMedico')

        print(fecha)
        print(hora)
        print(nota)
        print(idPaciente)
        print(idMedico)

        sql = "INSERT INTO Cita (fecha, hora, nota, idPaciente, idMedico) VALUES (%s, %s, %s, %s, %s)"
        data = (fecha, hora, nota, idPaciente, idMedico)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Cita agregada!'
    return jsonify(response_object)

@app.route('/tratamiento', methods=['GET', 'POST'])  
def tratamiento():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json(silent=True)
        inicio = post_data.get('inicio')
        fin = post_data.get('fin')
        Medicamento = post_data.get('Medicamento')
        dosis = post_data.get('dosis')
        frecuencia = post_data.get('frecuencia')
        idCita = post_data.get('idCita')

        print(inicio)
        print(fin)
        print(Medicamento)
        print(dosis)
        print(frecuencia)
        print(idCita)

        sql = "INSERT INTO Tratamiento (inicio, fin, Medicamento, dosis, frecuencia, idCita) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (inicio, fin, Medicamento, dosis, frecuencia, idCita)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        response_object['message'] = 'Tratamiento agregado!'
    return jsonify(response_object)

# PUT'S

@app.route('/paciente/<string:id>', methods=['PUT'])
def update_paciente(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json(silent=True)
        nombre = post_data.get('nombre')
        apellidop = post_data.get('apellidop')
        apellidom = post_data.get('apellidom')
        dni = post_data.get('dni')
        genero = post_data.get('genero')
        fnac = post_data.get('fnac')
        email = post_data.get('email')
        telef = post_data.get('telef')

        print(nombre)
        print(apellidop)
        print(apellidom)
        print(dni)
        print(genero)
        print(fnac)
        print(email)
        print(telef)

        cursor.execute ("UPDATE Paciente SET nombre = %s, apellidop = %s, apellidom = %s, dni = %s, genero = %s, fnac = %s, email = %s, telef = %s WHERE idPaciente = %s", 
        (nombre, apellidop, apellidom, dni, genero, fnac, email, telef, id))
        conn.commit()   
        cursor.close()
        response_object['message'] = 'Paciente actualizado!'
    return jsonify(response_object)

@app.route('/medico/<string:id>', methods=['PUT'])
def update_medico(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json(silent=True)
        nombreM = post_data.get('nombreM')
        apellidoPM = post_data.get('apellidoPM')
        apellidoMM = post_data.get('apellidoMM')
        dniM = post_data.get('dniM')
        generoM = post_data.get('generoM')
        emailM = post_data.get('emailM')
        fnacimientoM = post_data.get('fnacimientoM')
        numColegialM = post_data.get('numColegialM')
        especialidad = post_data.get('especialidad')

        print(nombreM)
        print(apellidoPM)
        print(apellidoMM)
        print(dniM)
        print(generoM)
        print(emailM)
        print(fnacimientoM)
        print(numColegialM)
        print(especialidad)

        cursor.execute ("UPDATE Medico SET nombreM = %s, apellidoPM = %s, apellidoMM = %s, dniM = %s, generoM = %s, emailM = %s, fnacimientoM = %s, numColegialM = %s, especialidad = %s WHERE idMedico = %s",
        (nombreM, apellidoPM, apellidoMM, dniM, generoM, emailM, fnacimientoM, numColegialM, especialidad, id))
        conn.commit()
        cursor.close()
        response_object['message'] = 'Medico actualizado!'
    return jsonify(response_object)

@app.route('/cita/<string:id>', methods=['PUT'])
def update_cita(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json(silent=True)
        fecha = post_data.get('fecha')
        hora = post_data.get('hora')
        nota = post_data.get('nota')
        idPaciente = post_data.get('idPaciente')
        idMedico = post_data.get('idMedico')

        print(fecha)
        print(hora)
        print(nota)
        print(idPaciente)
        print(idMedico)

        cursor.execute ("UPDATE Cita SET fecha = %s, hora = %s, nota = %s, idPaciente = %s, idMedico = %s WHERE idCita = %s",
        (fecha, hora, nota, idPaciente, idMedico, id))
        conn.commit()
        cursor.close()
        response_object['message'] = 'Cita actualizada!'
    return jsonify(response_object)

@app.route('/tratamiento/<string:id>', methods=['PUT'])
def update_tratamiento(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json(silent=True)
        inicio = post_data.get('inicio')
        fin = post_data.get('fin')
        Medicamento = post_data.get('Medicamento')
        dosis = post_data.get('dosis')
        frecuencia = post_data.get('frecuencia')
        idCita = post_data.get('idCita')

        print(inicio)
        print(fin)
        print(Medicamento)
        print(dosis)
        print(frecuencia)
        print(idCita)

        cursor.execute ("UPDATE Tratamiento SET inicio = %s, fin = %s, Medicamento = %s, dosis = %s, frecuencia = %s, idCita = %s WHERE idTratamiento = %s",
        (inicio, fin, Medicamento, dosis, frecuencia, idCita, id))
        conn.commit()
        cursor.close()
        response_object['message'] = 'Tratamiento actualizado!'
    return jsonify(response_object)

# DELETE'S

@app.route('/paciente/<string:id>', methods=['DELETE'])
def delete_paciente(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    response_object = {'status': 'success'}

    cursor.execute("DELETE FROM Paciente WHERE idPaciente = %s", [id])
    conn.commit()
    cursor.close()
    response_object['message'] = 'Paciente eliminado!'
    return jsonify(response_object)

@app.route('/medico/<string:id>', methods=['DELETE'])
def delete_medico(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    response_object = {'status': 'success'}

    cursor.execute("DELETE FROM Medico WHERE idMedico = %s", [id])
    conn.commit()
    cursor.close()
    response_object['message'] = 'Medico eliminado!'
    return jsonify(response_object)

@app.route('/cita/<string:id>', methods=['DELETE'])
def delete_cita(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    response_object = {'status': 'success'}

    cursor.execute("DELETE FROM Cita WHERE idCita = %s", [id])
    conn.commit()
    cursor.close()
    response_object['message'] = 'Cita eliminada!'
    return jsonify(response_object)

@app.route('/tratamiento/<string:id>', methods=['DELETE'])
def delete_tratamiento(id):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    response_object = {'status': 'success'}

    cursor.execute("DELETE FROM Tratamiento WHERE idTratamiento = %s", [id])
    conn.commit()
    cursor.close()
    response_object['message'] = 'Tratamiento eliminado!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
