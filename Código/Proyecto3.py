import random
class Pais:
    def __init__(self,codigo_fifa, nombre, continente, ranking_fifa):
        if not isinstance(codigo_fifa, str) or len(codigo_fifa) != 3:
            raise ValueError("El código FIFA debe ser una cadena de 3 caracteres.")
        else:
            self.codigo_fifa =codigo_fifa
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre del país debe ser una cadena no vacía.")
        else:
            self.nombre=nombre
        if not isinstance(continente,str):
            raise ValueError("El continente ingresado debe ser texto")
            if not SinEspacios(continente):
                raise ValueError("El continente no debe iniciar o terminar ocn espacios.")
        self.continente = ""
        self.ranking_fifa = 0
    def mostrar_datos(self):
        print(f"Código FIFA: {self.codigo_fifa}")
        
        print(f"Nombre: {self.nombre}")
        print(f"Continente: {self.continente}")
        print(f"Ranking FIFA: {self.ranking_fifa}")
def actualizar_datos(pais, codigo_fifa, nombre, continente, ranking_fifa):
    if codigo_fifa is not None:
        pais.codigo_fifa = codigo_fifa
    if nombre is not None:
        pais.nombre = nombre
    if continente is not None:
        pais.continente = continente
    if ranking_fifa is not None:
        pais.ranking_fifa = ranking_fifa

class Persona:
    def __init__(self, nombre, apellido,fecha_nacimiento,nacionalidad):
        if not Validaciones().debeser(nombre, str):
            print(Validaciones().debeser(nombre, str))
        else:
            self.nombre = nombre
            if not Validaciones().debeser(apellido, str):
                print(Validaciones().debeser(apellido, str))
            else:
                self.apellido = apellido
                if not Validaciones().debeser(fecha_nacimiento, str):
                    print(Validaciones().debeser(fecha_nacimiento, str))
                else:
                    self.fecha_nacimiento = fecha_nacimiento
                    if not Validaciones().debeser(nacionalidad, str):
                        print(Validaciones().debeser(nacionalidad, str))
                    else:
                        self.nacionalidad = nacionalidad
def mostrar_datos(self):
    print(f"Nombre: {self.nombre}")
    print(f"Apellido: {self.apellido}")
    print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
    print(f"Nacionalidad: {self.nacionalidad}") 


class Entrenador(Persona):
    def __init__(self,licencia,experiencia_anios,sistema_juego):
        if not Validaciones().debeser(licencia, str):
            print(Validaciones().debeser(licencia, str))
        else:
            self.licencia = licencia
            if not Validaciones().debeser(experiencia_anios, int) and experiencia_anios >= 0 and experiencia_anios <= 50:
                print(Validaciones().debeser(experiencia_anios, int))
            else:
                self.experiencia_anios = experiencia_anios
                if not Validaciones().debeser(sistema_juego, str):
                    print(Validaciones().debeser(sistema_juego, str))
                else:
                    self.sistema_juego = sistema_juego
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Licencia: {self.licencia}")
        print(f"Experiencia: {self.experiencia_anios} años")
        print(f"Sistema de Juego: {self.sistema_juego}")
    def actualizar_datos(self, licencia, experiencia, sistema_juego):
        if licencia is not None:
            self.licencia = licencia
        if experiencia is not None and isinstance(experiencia, int) and 0 <= experiencia <= 50:
            self.experiencia = experiencia
        if sistema_juego is not None:
            self.sistema_juego = sistema_juego
class Futbolista(Persona):
    def __init__(self,dorsal,posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles,asistencias,puntaje_individual):
        if isinstance(dorsal, int) and dorsal > 0 and dorsal <= 99:
            self.dorsal = dorsal
        else:
            raise ValueError("El dorsal debe ser un número entero entre 1 y 99.")
        if isinstance(posicion, str):
            self.posicion = posicion
        else:
            raise ValueError("La posición debe ser texto.")
        if isinstance(total_tarjetas_amarillas, int) and total_tarjetas_amarillas >= 0:
            self.total_tarjetas_amarillas = total_tarjetas_amarillas
        else:
            raise ValueError("El total de tarjetas amarillas debe ser un número entero mayor o igual a 0.")
        if isinstance(total_tarjetas_rojas, int) and total_tarjetas_rojas >= 0:
            self.total_tarjetas_rojas = total_tarjetas_rojas
        else:
            raise ValueError("El total de tarjetas  rojas debe ser un número entero mayor o igual a 0.")
              
        if isinstance(goles, int) and goles >= 0:
            self.goles = goles
        else:
            raise ValueError("Los goles deben ser un número entero mayor o igual a 0.")
        if isinstance(asistencias, int) and asistencias >= 0:
            self.asistencias = asistencias
        else:
        
            raise ValueError("Las asistencias deben ser un número entero mayor o igual a 0.")
        if puntaje_individual ==None:
            self.puntaje_individual = random.randint(4, 100)
        else:
            if isinstance(puntaje_individual, int) and puntaje_individual > 0 and puntaje_individual <= 100:
                self.puntaje_individual = puntaje_individual
            else:
                raise ValueError("El puntaje individual debe ser un número entero entre 0 y 100.")      
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Dorsal: {self.dorsal}")
        print(f"Posición: {self.posicion}")
        print(f"Total Tarjetas Amarillas: {self.total_tarjetas_amarillas}")
        print(f"Total Tarjetas Rojas: {self.total_tarjetas_rojas}")
        print(f"Goles: {self.goles}")
        print(f"Asistencias: {self.asistencias}")
        print(f"Puntaje Individual: {self.puntaje_individual}")
    def actualizar_datos(self, dorsal, posicion, total_tarjetas_amarillas, total_tarjetas_rojas, goles, asistencias, puntaje_individual):
        
        if isinstance(dorsal, int) and dorsal > 0 and dorsal <= 99 and dorsal!=None:
            self.dorsal = dorsal
        else:
            raise ValueError("El dorsal debe ser un número entero entre 1 y 99.")
        if isinstance(posicion, str) and posicion!=None:
            self.posicion = posicion
        else:
            raise ValueError("La posición debe ser texto.")
        if isinstance(total_tarjetas_amarillas, int) and total_tarjetas_amarillas >= 0 and total_tarjetas_amarillas!=None:
            self.total_tarjetas_amarillas = total_tarjetas_amarillas
        else:
            raise ValueError("El total de tarjetas amarillas debe ser un número entero mayor o igual a 0.")
        if isinstance(total_tarjetas_rojas, int) and total_tarjetas_rojas >= 0 and total_tarjetas_rojas!=None:
            self.total_tarjetas_rojas = total_tarjetas_rojas
        else:
            raise ValueError("El total de tarjetas  rojas debe ser un número entero mayor o igual a 0.")
              
        if isinstance(goles, int) and goles >= 0 and goles!=None:
            self.goles = goles
        else:
            raise ValueError("Los goles deben ser un número entero mayor o igual a 0.")
        if isinstance(asistencias, int) and asistencias >= 0 and asistencias!=None:
            self.asistencias = asistencias
        else:
            raise ValueError("Las asistencias deben ser un número entero mayor o igual a 0.")
        if puntaje_individual ==None:
            self.puntaje_individual = random.randint(4, 100)
        else:
            if (puntaje_individual).lower!="original":
                if isinstance(puntaje_individual, int) and puntaje_individual > 0 and puntaje_individual <= 100:
                    self.puntaje_individual = puntaje_individual
                else:
                    raise ValueError("El puntaje individual debe ser un número entero entre 0 y 100.")
    def registrar_gol(self):
        self.goles += 1
    def registrar_asistencia(self):
        self.asistencias += 1
    def registrar_tarjeta(self, tipo):
        if tipo == "amarilla":
            self.total_tarjetas_amarillas += 1
        elif tipo == "roja":
            self.total_tarjetas_rojas += 1
        else:
            print("Tipo de tarjeta inválido. Debe ser amarilla o roja.")
class Seleccion:
    codigo_equipo=0
    def __init__(self,pais,entrenador,jugadores,total_goles_favor,total_goles_contra,total_tarjetas_amarillas,total_tarjetas_rojas,fuerza_equipo):
        if not isinstance(pais,object) or not isinstance(entrenador,object):
           raise ValueError("El país y entrenador deben ser objetos válidos.") 
        else:
            self.pais = pais
            self.entrenador = entrenador
        if not isinstance(total_goles_favor, int) or total_goles_favor < 0:
            raise ValueError("El total de goles a favor debe ser un número entero mayor o igual a 0.")
        else:
            self.total_goles_favor = total_goles_favor
        if not isinstance(total_goles_contra, int) or total_goles_contra < 0:
            raise ValueError("El total de goles en contra debe ser un número entero mayor o igual a 0.")
        else:
            self.total_goles_contra = total_goles_contra
        if not isinstance(total_tarjetas_amarillas, int) or total_tarjetas_amarillas < 0:
            raise ValueError("El total de tarjetas amarillas debe ser un número entero mayor o igual a 0.")
        else:
            self.total_tarjetas_amarillas = total_tarjetas_amarillas
        if not isinstance(total_tarjetas_rojas, int) or total_tarjetas_rojas < 0:
            raise ValueError("El total de tarjetas rojas debe ser un número entero mayor o igual a 0.")
        else:
            self.total_tarjetas_rojas = total_tarjetas_rojas
       
        for jugador in jugadores:
            fuerza_equipo += jugador.puntaje_individual
        fuerza_equipo = (fuerza_equipo / len(jugadores))*0.6
        if entrenador.experiencia_anios*4>100:
            factor_entrenador= 100
        else:
            factor_entrenador=entrenador.experiencia_anios*4
        fuerza_equipo+=factor_entrenador*0.25
        factor_entrenador+=pais.ranking_fifa*0.15
       
       #jugadores,fuerza_equipo

#Emanuel (arriba)
class Validaciones:
    def __init__(self):
        pass
    def SinEspacios(self, dato):
        if dato[0] == " " or dato[-1] == " ":
            return "El dato no debe tener espacios al inicio o al final."
        return True
    def debeser(self, dato, tipo):
        if not isinstance(dato, tipo):
            return f"El dato {dato} debe ser del tipo {tipo}."
        return True
    def fecha_valida(self,fecha):
        try:
            datos=fecha.split("/")
            dia=int(datos[0])
            mes=int(datos[1])
            año=int(datos[2])
            if dia < 1 or dia > 31:
                return "El día debe estar entre 1 y 31."
            if mes < 1 or mes > 12:
                return "El mes debe estar entre 1 y 12."
            if año < 1900 or año >= 2026:
                return "El año debe estar entre 1900 y 2026."
            return True
        except:
            return "La fecha debe tener el formato DD/MM/AAAA."


    def fase_valida(self,fase):
        if not fase == "Dieciseisavos" or fase == "Octavos" or fase == "Cuartos" or fase == "Semifinales" or fase == "Final":
            return "La fase debe ser una existente"
            
        
# -----------------------------------------------------------------------------------
#Kerry

class Partido:
    def __init__(self,id_partido,equipo1, equipo2, fase, fecha):

        if not Validaciones().debeser(id_partido, int):
            print(Validaciones().debeser(id_partido,int))
        else: 
            self.id = id_partido
        if not Validaciones().debeser(equipo1, str):
            print(Validaciones().debeser(equipo1, str))
        else:
            self.equipo1 = equipo1
        
        if not Validaciones().debeser(equipo2, str):
            print(Validaciones().debeser(equipo2, str))
            
        else:
            self.equipo2 = equipo2
        
        if not Validaciones().fecha_valida(fecha):
            print(Validaciones().fecha_valida(fecha))
        else:
            self.fecha = fecha
        
        if not Validaciones().debeser(fase,str):
            print(Validaciones().debeser(fase,str))
        else:
            if not Validaciones().fase_valida(fase):
                print(Validaciones().fase_valida(fase))
            else:
                self.fase = fase
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.ganador = ""
        
    ############################################################################
    def simular(self, equipo1_fuerza, equipo2_fuerza):
    
        self.fuerza1 = equipo1_fuerza
        self.fuerza2 = equipo2_fuerza
        equipofuerte = 0
        equipodebil = 0

        if self.fuerza1 > self.fuerza2:
            fuerte = self.fuerza1
            debil = self.fuerza2
           
        else:
            fuerte = self.fuerza2
            debil = self.fuerza1
              
        self.diferencia = fuerte - debil

        if self.diferencia > 30:
            equipofuerte = random.randint(2,7)
            equipodebil = random.randint(0,3)
        
        elif self.diferencia > 15:
            equipofuerte = random.randint(1,5)
            equipodebil = random.randint(0,4)
            
        else:
            self.goles_equipo1 = random.randint(0,4)
            self.goles_equipo2 = random.randint(0,4)

        if self.diferencia > 15:
            if self.fuerza1 > self.fuerza2:
                self.goles_equipo1 = equipofuerte
                self.goles_equipo2 = equipodebil
            else:
                self.goles_equipo2 = equipofuerte
                self.goles_equipo1 = equipodebil
    #############################################################################
    
    
    #Validacion de empates para juegos de fase de grupos
    def generar_ganadores(self):
        if self.goles_equipo1 == self.goles_equipo2:
            print (f"Empate entre {self.equipo1} y {self.equip}  ")
        else:
            if self.goles_equipo1 > self.goles_equipo2:
                self.ganador = self.equipo1
                self.golestotal = self.goles_equipo1
            else:
                self.ganador = self.equipo2
                self.golestotal = self.goles_equipo2
        
            print (f"Ganador del partido: {self.ganador} con {self.golestotal} goles")
        
    def mostrar_resultados(self):
        return f"{self.equipo1} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo2}"

    
class Grupo:
    def __init__(self, nombre_grupo):
        if not Validaciones().debeser(nombre_grupo, str):
            print(Validaciones().debeser(nombre_grupo, str))
        else:
            self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []


    def agregar_equipo(self, seleccion):
        if len(self.equipos) >= 4:
            print("No se pueden agregar más equipos al grupo.")
            return
        if not Validaciones().debeser(seleccion, str):
            print(Validaciones().debeser(seleccion, str))
        else:
            self.equipos += [seleccion]
        


















