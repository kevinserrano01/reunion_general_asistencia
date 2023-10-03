import datetime

fechaActual = datetime.date.today()
fecha_actual_formateada = fechaActual.strftime("%d-%m-%Y")

class Config:
    NOMBRE_ARCHIVO = "Asistencia_Reunion_General.xlsx",
    HOJA = fecha_actual_formateada