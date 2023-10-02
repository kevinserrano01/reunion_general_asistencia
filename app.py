from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import openpyxl
from openpyxl import load_workbook, Workbook # read excel


app = Flask(__name__)

# Mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123987'
app.config['MYSQL_DB'] = 'reunion_general'
mysql = MySQL(app)

# settings
app.secret_key = 'mysecretkey' # para habilitar el mensaje de flash()

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    sql = """SELECT * FROM reunion_general.hermanos;"""
    cur.execute(sql)
    data = cur.fetchall()

    totalHermanos = len(data)
    return render_template('index.html', usuarios=data, totalUsuarios=totalHermanos)


@app.route('/agregar_usuario', methods = ['POST'])
def add_user():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        obervacion = request.form['observacion']

        cur = mysql.connection.cursor()
        sql = """
                INSERT INTO reunion_general.hermanos (nombre, apellido, observacion)
                VALUES (%s, %s, %s)
            """
        params = (nombre, apellido, obervacion)
        cur.execute(sql, params)
        mysql.connection.commit() # Save changes
        flash('Usuario agregado exitosamente!')
    return redirect(url_for('index')) # redireccionar a la funcion principal 'index'.


@app.route('/edit/<id>')
def get_user(id):
    cur = mysql.connection.cursor()
    sql = """
            SELECT * FROM reunion_general.hermanos
            WHERE hermano_id = %s
        """
    params = id,
    cur.execute(sql, params)
    data = cur.fetchall()
    return render_template('edit_contact.html', usuario = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        observacion = request.form['observacion']

        cur = mysql.connection.cursor()
        sql = """
                UPDATE reunion_general.hermanos
                SET nombre = %s, apellido = %s, observacion = %s
                WHERE hermano_id = %s
            """
        params = (nombre, apellido, observacion, id)
        cur.execute(sql, params)
        mysql.connection.commit() # Save changes
        flash('Usuario actualizado exitosamente!')
    return redirect(url_for('index')) # Redireccionamos a la pantalla principal

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    sql = "DELETE FROM usuarios WHERE usuario_id = %s"
    params = id,
    cur.execute(sql, params)
    mysql.connection.commit() # Save changes
    flash('Usuario Eliminado exitosamente!')
    return redirect(url_for('index'))


@app.route('/exportar')
def exportar_a_excel():
    cur = mysql.connection.cursor()
    sql = """SELECT usuarios.nombre, usuarios.apellido, usuarios.edad, DATE_FORMAT(usuarios.fecha, '%Y-%m-%d') as fecha, DATE_FORMAT(usuarios.hora, '%H:%i:%s') as hora, iglesias.nombre as iglesia
            FROM iglesias
            INNER JOIN usuarios ON iglesias.iglesia_id = usuarios.iglesia"""
    cur.execute(sql)
    data = cur.fetchall()

    for joven in data:
        # Abre el archivo Excel existente o crea uno nuevo si no existe
        try:
            libro_excel = load_workbook("Asistencia-02-10-2023.xlsx")
            hoja = libro_excel.active
        except FileNotFoundError:
            libro_excel = Workbook()
            hoja = libro_excel.active
            hoja.append([["Nombre", "Apellido", "Hora"]])

        # Añadir los nuevos datos debajo de los existentes
        hoja.append([joven[0], joven[1], joven[2], joven[3], joven[4], joven[5]])

        # Guardar el libro de Excel
        libro_excel.save("Asistencia-02-10-2023.xlsx")

    flash('Usuarios exportados exitosamente!')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(port = 4000, debug = True)