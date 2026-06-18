import random
class Pais:
    def __init__(self,codigo_fifa, nombre, continente, ranking_fifa):
        if not isinstance(codigo_fifa, str) or len(codigo_fifa) != 3:
            print("El código FIFA debe ser una cadena de 3 caracteres.")
        else:
            self.codigo_fifa =codigo_fifa
        if not isinstance(nombre, str) or not nombre:
            print("El nombre del país debe ser una cadena no vacía.")
        self.nombre = ""
        self.continente = ""
        self.ranking_fifa = 0
    def mostrar_datos(self):
        print(f"Código FIFA: {self.codigo_fifa}")
        
        print(f"Nombre: {self.nombre}")
        print(f"Continente: {self.continente}")
        print(f"Ranking FIFA: {self.ranking_fifa}")
def actualizar_datos(pais, codigo_fifa=None, nombre=None, continente=None, ranking_fifa=None):
    if codigo_fifa is not None:
        pais.codigo_fifa = codigo_fifa
    if nombre is not None:
        pais.nombre = nombre
    if continente is not None:
        pais.continente = continente
    if ranking_fifa is not None:
        pais.ranking_fifa = ranking_fifa




#Emanuel
class Validaciones:
    def __init__(self):
        pass
    def SinEspacios(self, dato):
        if dato[0] == " " or dato[-1] == " ":
            return "El dato no debe tener espacios al inicio o al final."
        return True
# -----------------------------------------------------------------------------------
#Kerry

class Partido:
    def __init__(self,equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.ganador = ""
        
        
    def simular(self):
        self.goles_equipo1 = random.randit(0,6)
        self.goles|_equipo2 = random.randit(0,6)

    
    def generar_ganadores(self):
        if self.goles_equipo1 > self.goles_equipo2:
            self.ganador == self.equipo1
        else:
            self.ganador == self.equipo2
        
        
    def mostrar_resultados(self):
        return f"{self.equipo1} {self.goles_equipo1} - {self.goles_equipos2} {self.equipo2}"

    





















