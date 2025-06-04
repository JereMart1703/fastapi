#primero importamos las librerias necesarias , en este caso de la carpeta modelo , hospitales
from data.modelo.hospitales import Hospital

class DaoHospitales:
    def get_all(self, db) -> list[Hospital]:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM hospitales") # Consulta para obtener todos los hospitales
        filas = cursor.fetchall() # Obtiene todas las filas de la consulta
        hospitales = list[Hospital]=[] # Inicializa una lista de hospitales
        for hospital in filas:
            # Crea un objeto Hospital por cada fila obtenida
            hospital = Hospital(id=hospital[0], nombre=hospital[1], numero_pacientes=hospital[2])
            hospitales.append(hospital)
        cursor.close()
        return hospitales