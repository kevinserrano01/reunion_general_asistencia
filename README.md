## 📌 APP DE ASISTENCIA 

Desarrollé una aplicación diseñada con Python, Flask, HTML, CSS, Javascript, Bootstrap y MySQL para simplificar el proceso de tomar asistencia en clases secundarias y universitarias. La aplicación permite a los profesores registrar la asistencia de los estudiantes de manera rápida y precisa utilizando sus dispositivos móviles o computadoras. Además, la aplicación genera informes mediante un archivo Excel que muestran estadísticas detalladas sobre la asistencia de los estudiantes como la hora de llegada, lo que facilita el seguimiento del progreso y la participación en clase. En resumen, mi aplicación optimiza el proceso de toma de asistencia, ahorrando tiempo a los profesores, y proporcionando información útil para mejorar la experiencia educativa.

La aplicacion tiene gran variedad de funciones:

- **Listado de Alumnos**: Listado de Alumnos presentes.

- **Crear Alumno**: Poner presente a un alumno anotando su nombre, apellido y observacion(no obligatorio).

- **Editar Alumno**: Puede editar el nombre y apellido del alumno en caso de haber un error ortografico.

- **Eliminar Alumno**: Puede eliminar un alumno en caso de que se halla duplicado ese alumno o por equivocacion de clase.

- **Limpiar lista**: Una vez finalizada la asistencia se guarda en un archivo excel y recien puede limpiar la lista en pantalla para tomar asistencia en otra clase.

- **Exportar asistencia**: Al finalizar la toma de asistencia puede guardar esos alumnos presentes en un archivo Excel con la fecha actual.

- **Total de presentes**: Muestra el total de alumnos presnete en clase en la parte superior derecha de la App.

## 🔌 INSTALAR APLICACION

Clonar el repositorio.

```bash
  git clone https://github.com/kevinserrano01/reunion_general_asistencia.git
```

Acceder a la carpeta principal que se crea luego de clonar el repositorio.

```bash
  cd reunion_general_asistencia
```

Instalar las dependencias.

```bash
  pip install -r requirements.txt
```
Ejecutar el archivo "app.py" para ejecutar la Aplicacion.

```bash
  py app.py
```