import psycopg2

class Conexion:

    def __init__(self):
        """ Metodo contructor de la conexión
        
        Se retorna una instancia de la base de datos
        """
        self.__con = psycopg2.connect("dbname=pruebas user=postgres host=localhost password=dav123")

    def getConexion(self):
        return self.__con