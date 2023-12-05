from conexion.conexion import Conexion

class CiudadDAO:
    def getCiudades(self):
        ciudadSQL = """
            SELECT id_ciudad, descri_ciudad
            FROM ciudad
            """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(ciudadSQL)
            lista_ciudades = cur.fetchall()
            return lista_ciudades
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()

    def getCiudadById(self, id):
        
        ciudadSQL = """
            SELECT id_ciudad, descri_ciudad
            FROM ciudad WHERE id_ciudad = %s
        """
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:    
            cur.execute(ciudadSQL, (id,))
            ciudad = cur.fetchone()
            if ciudad:
                return { 'id_ciudad': ciudad[0], 'descri_ciudad': ciudad[1]}
            return None
        except con.Error as e:
            print(f"pgcode = {e.pgcode} , mensaje = {e.pgerror}")            

        finally:
            cur.close()
            con.close()