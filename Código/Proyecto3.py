import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import scrolledtext

grupos = ["Grupo A", "Grupo B", "Grupo C", "Grupo D", "Grupo E", "Grupo F", "Grupo G", "Grupo H", "Grupo I", "Grupo J", "Grupo K", "Grupo L",]

paises = []
entrenadores = []
selecciones = []

#E:accion, nombre del archivo, linea, linea nueva
#S:true o false si busca, o nada si modifica el archivo
#R:la accion debe ser agg, buscar, elim o act
#objetivo:agregar, buscar, eliminar o actualizar una linea en un archivo
def gestion_archivos(accion, nombre, linea, linea_nueva):
    try:
        archivo = open(nombre, "r")
        lineas = archivo.readlines()
        archivo.close()

        if accion == "agg":
            archivo = open(nombre, "a")
            archivo.write(linea + "\n")
            archivo.close()

        elif accion == "buscar":
            for i in lineas:
                if i.strip() == linea:
                    return True
            return False

        elif accion == "elim":
            aux = ""
            for i in lineas:
                if i.strip() != linea:
                    aux += i
            archivo = open(nombre, "w")
            archivo.write(aux)
            archivo.close()

        elif accion == "act":
            if linea_nueva == None:
                print("Se necesita linea_nueva para actualizar.")
                return
            aux = ""
            for i in lineas:
                if i.strip() == linea:
                    aux += linea_nueva + "\n"
                else:
                    aux += i
            archivo = open(nombre, "w")
            archivo.write(aux)
            archivo.close()

    except FileNotFoundError:
        print(f"Archivo {nombre} no encontrado.")

#E:ninguna
#S:ninguna
#R:los archivos deben existir para cargar datos
#objetivo:cargar paises, entrenadores, selecciones y jugadores desde los archivos
def cargar_todo():
    global paises
    global entrenadores
    global selecciones

    try:
        archivo = open("paises.txt", "r")
        for linea in archivo.readlines():
            datos = linea.strip().split(",")
            if len(datos) < 4: 
                print(f"Linea invalida en paises.txt: {linea.strip()}")
                continue
            try: # fix: si un dato esta mal no explota todo
                paises += [Pais(datos[0], datos[1], datos[2], int(datos[3]), False)]
            except ValueError as e:
                print(f"Error al cargar pais: {e}")
        archivo.close()
    except FileNotFoundError:
        pass

    try:
        archivo = open("entrenadores.txt", "r")
        for linea in archivo.readlines():
            datos = linea.strip().split(",")
            if len(datos) < 8: # fix: linea incompleta en archivo
                print(f"Linea invalida en entrenadores.txt: {linea.strip()}")
                continue
            try: # fix: si un dato esta mal no explota todo
                entrenadores += [(datos[0], Entrenador(datos[1], datos[2], datos[3], datos[4], datos[5], int(datos[6]), datos[7], False))]
            except ValueError as e:
                print(f"Error al cargar entrenador: {e}")
        archivo.close()
    except FileNotFoundError:
        pass

    try:
        archivo = open("selecciones.txt", "r")
        for linea in archivo.readlines():
            datos = linea.strip().split(",")
            if len(datos) < 1: # fix: linea incompleta en archivo
                print(f"Linea invalida en selecciones.txt: {linea.strip()}")
                continue
            for p in paises:
                if p.codigo_fifa == datos[0]:
                    for codigo, entrenador in entrenadores:
                        if codigo == datos[0]:
                            try: # fix: si un dato esta mal no explota todo
                                selecciones += [Seleccion(p, entrenador, False)]
                            except ValueError as e:
                                print(f"Error al cargar seleccion: {e}")
        archivo.close()
    except FileNotFoundError:
        pass

    try:
        archivo = open("jugadores.txt", "r")
        for linea in archivo.readlines():
            datos = linea.strip().split(",")
            if len(datos) < 12: # fix: linea incompleta en archivo
                print(f"Linea invalida en jugadores.txt: {linea.strip()}")
                continue
            try: # fix: si un dato esta mal no explota todo
                codigo_pais = datos[0]
                jugador = Futbolista(datos[1], datos[2], datos[3], datos[4], int(datos[5]), datos[6], int(datos[7]), int(datos[8]), int(datos[9]), int(datos[10]), int(datos[11]), False)
                encontrado = False # fix: si no encuentra la seleccion avisa
                for seleccion in selecciones:
                    if seleccion.pais.codigo_fifa == codigo_pais:
                        seleccion.jugadores += [jugador]
                        encontrado = True
                if not encontrado:
                    print(f"No se encontro seleccion para el jugador {datos[1]} {datos[2]}")
            except ValueError as e:
                print(f"Error al cargar jugador: {e}")
        archivo.close()
    except FileNotFoundError:
        pass

class Validaciones:
    def __init__(self):
        pass

    #E:dato
    #S:true o un error si tiene espacios
    #R:el dato no debe estar vacio
    #objetivo:validar que un dato no inicie ni termine con espacios
    def SinEspacios(self, dato):
        if dato == "":
            raise ValueError("El dato no debe tener espacios al inicio o al final.")
        if dato[0] == " " or dato[-1] == " ":
            raise ValueError("El dato no debe tener espacios al inicio o al final.")
        return True

    #E:dato, tipo esperado
    #S:true o mensaje de error
    #R:ninguna
    #objetivo:validar que un dato sea del tipo esperado
    def debeser(self, dato, tipo):
        if not isinstance(dato, tipo):
            return f"El dato {dato} debe ser del tipo {tipo}."
        return True

    #E:fecha
    #S:true o mensaje de error
    #R:la fecha debe venir en formato dia mes año separados por barra
    #objetivo:validar que una fecha sea valida
    def fecha_valida(self, fecha):
        try:
            datos = fecha.split("/")
            dia = int(datos[0])
            mes = int(datos[1])
            año = int(datos[2])
            if dia < 1 or dia > 31:
                return "El día debe estar entre 1 y 31."
            if mes < 1 or mes > 12:
                return "El mes debe estar entre 1 y 12."
            if año < 1900 or año > 2026:
                return "El año debe estar entre 1900 y 2026."
            return True
        except:
            return "La fecha debe tener el formato DD/MM/AAAA."

    #E:lista de jugadores
    #S:los once jugadores con mayor puntaje
    #R:ninguna
    #objetivo:ordenar los jugadores y devolver los once mejores
    def onceGrandes(self, lista):
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                if lista[i].puntaje_individual > lista[j].puntaje_individual:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        return lista[0:11]

    #E:jugadores, entrenador, pais
    #S:el valor de fuerza del equipo
    #R:ninguna
    #objetivo:calcular la fuerza de un equipo segun sus jugadores entrenador y pais
    def fuerza_equipo_def(self, jugadores, entrenador, pais):
        fuerza_equipo = 0
        for jugador in jugadores:
            fuerza_equipo += jugador.puntaje_individual
        fuerza_equipo = (fuerza_equipo / 11) * 0.6
        if entrenador.experiencia_anios * 4 > 100:
            factor_entrenador = 100
        else:
            factor_entrenador = entrenador.experiencia_anios * 4
        fuerza_equipo += factor_entrenador * 0.25
        fuerza_equipo += (100 - pais.ranking_fifa) * 0.15
        return fuerza_equipo

    #E:fase
    #S:true o mensaje de error
    #R:la fase debe ser una de las existentes
    #objetivo:validar que la fase ingresada exista
    def fase_valida(self, fase):
        if not (fase.lower() == "dieciseisavos" or fase.lower() == "octavos" or fase.lower() == "cuartos" or fase.lower() == "semifinales" or fase.lower() == "final"):
            return "La fase debe ser una existente"
        return True

class Pais:
    #E:codigo fifa, nombre, continente, ranking fifa, guardar
    #S:instancia del pais
    #R:el pais no debe existir ya, el codigo fifa debe tener 3 caracteres
    #objetivo:crear un pais y guardarlo en el archivo si se indica
    def __init__(self, codigo_fifa, nombre, continente, ranking_fifa, guardar):
        global paises
        for p in paises:
            if p.codigo_fifa == codigo_fifa:
                raise ValueError("El país ya existe.") 
        if not isinstance(codigo_fifa, str) or len(codigo_fifa) != 3:
            raise ValueError("El código FIFA debe ser una cadena de 3 caracteres.")
        else:
            self.codigo_fifa = codigo_fifa
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre del país debe ser una cadena no vacía.")
        else:
            self.nombre = nombre
        if not isinstance(continente, str):
            raise ValueError("El continente ingresado debe ser texto")
        else:
            if Validaciones().SinEspacios(continente) != True:
                raise ValueError("El continente no debe iniciar o terminar con espacios.")
            else:
                self.continente = continente
        if not isinstance(ranking_fifa, int):
            raise ValueError("El rank FIFA debe ser un numero")
        self.ranking_fifa = ranking_fifa
        paises += [self]
        if guardar:
            gestion_archivos("agg", "paises.txt", f"{self.codigo_fifa},{self.nombre},{self.continente},{self.ranking_fifa}", None)

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar los datos del pais
    def mostrar_datos(self):
        print(f"Código FIFA: {self.codigo_fifa}")
        print(f"Nombre: {self.nombre}")
        print(f"Continente: {self.continente}")
        print(f"Ranking FIFA: {self.ranking_fifa}")

    #E:codigo fifa, nombre, continente, ranking fifa
    #S:mensaje de error si algun dato es invalido
    #R:los datos a actualizar deben ser validos
    #objetivo:actualizar los datos del pais
    def actualizar_datos(self, codigo_fifa, nombre, continente, ranking_fifa):
        linea_vieja = f"{self.codigo_fifa},{self.nombre},{self.continente},{self.ranking_fifa}"
        if codigo_fifa != None:
            if not isinstance(codigo_fifa, str) or len(codigo_fifa) != 3: 
                return "El código FIFA debe ser una cadena de 3 caracteres."
            self.codigo_fifa = codigo_fifa
        if nombre != None:
            if not isinstance(nombre, str) or nombre=="":
                return "El nombre del país debe ser una cadena no vacía."
            self.nombre = nombre
        if continente != None:
            if not isinstance(continente, str):
                return "El continente ingresado debe ser texto."
            self.continente = continente
        if ranking_fifa != None:
            if not isinstance(ranking_fifa, int): 
                return "El rank FIFA debe ser un numero."
            self.ranking_fifa = ranking_fifa
        gestion_archivos("act", "paises.txt", linea_vieja, f"{self.codigo_fifa},{self.nombre},{self.continente},{self.ranking_fifa}")

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:eliminar el pais de la lista y del archivo
    def eliminar(self):
        global paises
        aux = []
        for p in paises:
            if p.codigo_fifa != self.codigo_fifa:
                aux += [p]
        paises = aux
        gestion_archivos("elim", "paises.txt", f"{self.codigo_fifa},{self.nombre},{self.continente},{self.ranking_fifa}", None)

    #E:codigo fifa
    #S:el pais encontrado o nada
    #R:ninguna
    #objetivo:buscar un pais por su codigo fifa
    def buscar(codigo_fifa):
        for p in paises:
            if p.codigo_fifa == codigo_fifa:
                return p
        return None

class Persona:
    #E:nombre, apellido, fecha de nacimiento, nacionalidad
    #S:instancia de la persona
    #R:cada dato debe ser texto
    #objetivo:crear una persona con sus datos basicos
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad):
        if Validaciones().debeser(nombre, str) != True:
            print(Validaciones().debeser(nombre, str))
        else:
            self.nombre = nombre
            if Validaciones().debeser(apellido, str) != True:
                print(Validaciones().debeser(apellido, str))
            else:
                self.apellido = apellido
                if Validaciones().debeser(fecha_nacimiento, str) != True:
                    print(Validaciones().debeser(fecha_nacimiento, str))
                else:
                    self.fecha_nacimiento = fecha_nacimiento
                    if Validaciones().debeser(nacionalidad, str) != True:
                        print(Validaciones().debeser(nacionalidad, str))
                    else:
                        self.nacionalidad = nacionalidad

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar los datos de la persona
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"Nacionalidad: {self.nacionalidad}")

class Entrenador(Persona):
    #E:nombre, apellido, fecha de nacimiento, nacionalidad, licencia, experiencia, sistema de juego, guardar
    #S:instancia del entrenador
    #R:la experiencia debe estar entre 0 y 50 años
    #objetivo:crear un entrenador y guardarlo en el archivo si se indica
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, licencia, experiencia_anios, sistema_juego, guardar):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)
        if not Validaciones().debeser(licencia, str):
            print(Validaciones().debeser(licencia, str))
        else:
            self.licencia = licencia
            if not Validaciones().debeser(experiencia_anios, int):
                print(Validaciones().debeser(experiencia_anios, int))
            elif not (experiencia_anios >= 0 and experiencia_anios <= 50):
                print("La experiencia en años debe ser de 0 a 50 años")
            else:
                self.experiencia_anios = experiencia_anios
                if not Validaciones().debeser(sistema_juego, str):
                    print(Validaciones().debeser(sistema_juego, str))
                else:
                    self.sistema_juego = sistema_juego
        if guardar:
            gestion_archivos("agg", "entrenadores.txt", f"{self.nombre},{self.apellido},{self.fecha_nacimiento},{self.nacionalidad},{self.licencia},{self.experiencia_anios},{self.sistema_juego}", None)

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar los datos del entrenador
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Licencia: {self.licencia}")
        print(f"Experiencia: {self.experiencia_anios} años")
        print(f"Sistema de Juego: {self.sistema_juego}")

    #E:licencia, experiencia, sistema de juego
    #S:mensaje de error si algun dato es invalido
    #R:la experiencia debe estar entre 0 y 50 años
    #objetivo:actualizar los datos del entrenador
    def actualizar_datos(self, licencia, experiencia, sistema_juego):
        linea_vieja = f"{self.nombre},{self.apellido},{self.fecha_nacimiento},{self.nacionalidad},{self.licencia},{self.experiencia_anios},{self.sistema_juego}"
        if licencia != None:
            if not isinstance(licencia, str): 
                return "La licencia debe ser texto."
            self.licencia = licencia
        if experiencia != None:
            if not isinstance(experiencia, int) or not (0 <= experiencia <= 50): 
                return "La experiencia debe ser un numero entre 0 y 50."
            self.experiencia_anios = experiencia
        if sistema_juego != None:
            if not isinstance(sistema_juego, str): 
                return "El sistema de juego debe ser texto."
            self.sistema_juego = sistema_juego
        gestion_archivos("act", "entrenadores.txt", linea_vieja, f"{self.nombre},{self.apellido},{self.fecha_nacimiento},{self.nacionalidad},{self.licencia},{self.experiencia_anios},{self.sistema_juego}")

    #E:codigo del pais
    #S:mensaje si no se encuentra el entrenador
    #R:ninguna
    #objetivo:eliminar el entrenador de la lista y del archivo
    def eliminar(self, codigo_pais):
        global entrenadores
        aux = []
        encontrado = False
        for i in range(len(entrenadores)):
            if entrenadores[i][0] != codigo_pais:
                aux += [entrenadores[i]]
            else:
                encontrado = True
                gestion_archivos("elim", "entrenadores.txt", f"{self.nombre},{self.apellido},{self.fecha_nacimiento},{self.nacionalidad},{self.licencia},{self.experiencia_anios},{self.sistema_juego}", None)
        if not encontrado:
            return "Entrenador no encontrado."
        entrenadores = aux

    #E:codigo del pais
    #S:el entrenador encontrado o nada
    #R:ninguna
    #objetivo:buscar un entrenador por el codigo de su pais
    def buscar(codigo_pais):
        for i in range(len(entrenadores)):
            if entrenadores[i][0] == codigo_pais:
                return entrenadores[i][1]
        return None

class Futbolista(Persona):
    #E:nombre, apellido, fecha de nacimiento, nacionalidad, dorsal, posicion, tarjetas amarillas, tarjetas rojas, goles, asistencias, puntaje individual, guardar
    #S:instancia del futbolista
    #R:el dorsal debe estar entre 1 y 99, el puntaje debe estar entre 0 y 100
    #objetivo:crear un futbolista con sus datos y estadisticas
    def __init__(self, nombre, apellido, fecha_nacimiento, nacionalidad, dorsal, posicion, total_tarjetas_amarillas, tarjetas_roj, goles, asistencias, puntaje_individual, guardar):
        Persona.__init__(self, nombre, apellido, fecha_nacimiento, nacionalidad)
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
        if isinstance(tarjetas_roj, int) and tarjetas_roj >= 0:
            self.tarjetas_roj = tarjetas_roj
        else:
            raise ValueError("El total de tarjetas rojas debe ser un número entero mayor o igual a 0.")
        if isinstance(goles, int) and goles >= 0:
            self.goles = goles
        else:
            raise ValueError("Los goles deben ser un número entero mayor o igual a 0.")
        if isinstance(asistencias, int) and asistencias >= 0:
            self.asistencias = asistencias
        else:
            raise ValueError("Las asistencias deben ser un número entero mayor o igual a 0.")
        if puntaje_individual == None:
            self.puntaje_individual = random.randint(4, 100)
        else:
            if isinstance(puntaje_individual, int) and puntaje_individual > 0 and puntaje_individual <= 100:
                self.puntaje_individual = puntaje_individual
            else:
                raise ValueError("El puntaje individual debe ser un número entero entre 0 y 100.")

    #E:ninguna
    #S:los datos del jugador en una sola linea
    #R:ninguna
    #objetivo:armar la linea de texto con los datos del jugador
    def linea(self):
        return f"{self.nombre},{self.apellido},{self.fecha_nacimiento},{self.nacionalidad},{self.dorsal},{self.posicion},{self.total_tarjetas_amarillas},{self.tarjetas_roj},{self.goles},{self.asistencias},{self.puntaje_individual}"

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar los datos del futbolista
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Dorsal: {self.dorsal}")
        print(f"Posición: {self.posicion}")
        print(f"Total Tarjetas Amarillas: {self.total_tarjetas_amarillas}")
        print(f"Total Tarjetas Rojas: {self.tarjetas_roj}")
        print(f"Goles: {self.goles}")
        print(f"Asistencias: {self.asistencias}")
        print(f"Puntaje Individual: {self.puntaje_individual}")

    #E:dorsal, posicion, tarjetas amarillas, tarjetas rojas, goles, asistencias, puntaje individual
    #S:mensaje de error si algun dato es invalido
    #R:el dorsal debe estar entre 1 y 99, el puntaje debe estar entre 0 y 100
    #objetivo:actualizar los datos del futbolista
    def actualizar_datos(self, dorsal, posicion, total_tarjetas_amarillas, tarjetas_roj, goles, asistencias, puntaje_individual):
        linea_vieja = self.linea()
        if dorsal != None:
            if isinstance(dorsal, int) and dorsal > 0 and dorsal <= 99:
                self.dorsal = dorsal
            else:
                return "El dorsal debe ser un número entero entre 1 y 99." 
        if posicion != None:
            if isinstance(posicion, str):
                self.posicion = posicion
            else:
                return "La posición debe ser texto." # 
        if total_tarjetas_amarillas != None:
            if isinstance(total_tarjetas_amarillas, int) and total_tarjetas_amarillas >= 0:
                self.total_tarjetas_amarillas = total_tarjetas_amarillas
            else:
                return "El total de tarjetas amarillas debe ser un número entero mayor o igual a 0." 
        if tarjetas_roj != None:
            if isinstance(tarjetas_roj, int) and tarjetas_roj >= 0:
                self.tarjetas_roj = tarjetas_roj
            else:
                return "El total de tarjetas rojas debe ser un número entero mayor o igual a 0." 
        if goles != None:
            if isinstance(goles, int) and goles >= 0:
                self.goles = goles
            else:
                return "Los goles deben ser un número entero mayor o igual a 0." # fix: retorna str en vez de raise
        if asistencias != None:
            if isinstance(asistencias, int) and asistencias >= 0:
                self.asistencias = asistencias
            else:
                return "Las asistencias deben ser un número entero mayor o igual a 0." # fix: retorna str en vez de raise
        if puntaje_individual == None:
            self.puntaje_individual = random.randint(4, 100)
        else:
            if isinstance(puntaje_individual, int) and puntaje_individual > 0 and puntaje_individual <= 100:
                self.puntaje_individual = puntaje_individual
            else:
                return "El puntaje individual debe ser un número entero entre 0 y 100." # fix: retorna str en vez de raise
        gestion_archivos("act", "jugadores.txt", linea_vieja, self.linea())

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:sumar un gol al jugador y actualizar el archivo
    def registrar_gol(self):
        linea_vieja = self.linea()
        self.goles += 1
        gestion_archivos("act", "jugadores.txt", linea_vieja, self.linea())

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:sumar una asistencia al jugador y actualizar el archivo
    def registrar_asistencia(self):
        linea_vieja = self.linea()
        self.asistencias += 1
        gestion_archivos("act", "jugadores.txt", linea_vieja, self.linea())

    #E:tipo de tarjeta
    #S:mensaje de error si el tipo no es valido
    #R:el tipo debe ser amarilla o roja
    #objetivo:sumar una tarjeta al jugador y actualizar el archivo
    def registrar_tarjeta(self, tipo):
        linea_vieja = self.linea()
        if tipo.lower() == "amarilla":
            self.total_tarjetas_amarillas += 1
        elif tipo.lower() == "roja":
            self.tarjetas_roj += 1
        else:
            return "Tipo de tarjeta inválido. Debe ser amarilla o roja." # fix: retorna str para messagebox
        gestion_archivos("act", "jugadores.txt", linea_vieja, self.linea())

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar el dorsal del jugador
    def dorsal2(self):
        print(self.dorsal)

class Seleccion:
    codigo_equipo = 0

    #E:pais, entrenador, guardar
    #S:instancia de la seleccion
    #R:el pais no debe tener ya una seleccion
    #objetivo:crear una seleccion con su pais y entrenador
    def __init__(self, pais, entrenador, guardar):
        global selecciones
        for s in selecciones:
            if s.pais.codigo_fifa == pais.codigo_fifa:
                raise ValueError("Ya existe una seleccion para ese país.") # fix: retorna str para messagebox
        if not isinstance(pais, Pais) or not isinstance(entrenador, Entrenador):
            raise ValueError("El país y entrenador deben ser objetos válidos.")
        else:
            self.pais = pais
            self.entrenador = entrenador
        self.jugadores = []
        self.goles_favor = 0
        self.goles_contra = 0
        self.total_tarjetas_amarillas = 0
        self.tarjetas_roj = 0
        Seleccion.codigo_equipo += 1
        self.contador_equipos = Seleccion.codigo_equipo
        self.total_goles_favor = 0
        self.total_goles_contra = 0
        self.fuerza_equipo = 0
        selecciones += [self]
        if guardar:
            gestion_archivos("agg", "selecciones.txt", f"{self.pais.codigo_fifa}", None)

    #E:ninguna
    #S:los datos de la seleccion en una sola linea
    #R:ninguna
    #objetivo:armar la linea de texto con los datos de la seleccion
    def linea(self):
        return f"{self.pais.codigo_fifa},{self.total_goles_favor},{self.total_goles_contra},{self.total_tarjetas_amarillas},{self.tarjetas_roj}"

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar los datos de la seleccion y sus jugadores
    def mostrar_datos(self):
        print("Jugadores")
        for i in self.jugadores:
            i.mostrar_datos()
        print(f"""
        Total Goles: {self.goles_favor}
        Total Goles en contra: {self.goles_contra}
        Total amarillas: {self.total_tarjetas_amarillas}
        Total Rojas: {self.tarjetas_roj}
        Fuerza equipo: {self.fuerza_equipo}
        Pais: {self.pais.nombre}
        Entrenador: {self.entrenador.nombre} {self.entrenador.apellido}
        """)

    #E:futbolista
    #S:mensaje de error si no se puede agregar
    #R:la seleccion debe tener menos de 23 jugadores y el dorsal no debe repetirse
    #objetivo:agregar un jugador a la seleccion
    def agregar_jugador(self, futbolista):
        if not isinstance(futbolista, Futbolista):
            return "El futbolista no es valido." # fix: mensaje mas claro
        if len(self.jugadores) >= 23: # fix: era > 23, permitia 24
            return "Maximo de jugadores alcanzado."
        for i in self.jugadores:
            if i.dorsal == futbolista.dorsal:
                return "Ya existe un jugador con ese dorsal." # fix: mensaje mas claro
        self.jugadores += [futbolista]
        gestion_archivos("agg", "jugadores.txt", f"{self.pais.codigo_fifa},{futbolista.linea()}", None)

    #E:dorsal
    #S:mensaje de error si no se encuentra el jugador
    #R:debe haber jugadores en la seleccion
    #objetivo:eliminar un jugador de la seleccion por su dorsal
    def eliminar_jugador(self, dorsal):
        if not isinstance(dorsal, int):
            return "El dorsal debe ser un numero entero." # fix: mensaje mas claro
        if len(self.jugadores) == 0:
            return "No hay jugadores en la seleccion." # fix: mensaje mas claro
        aux = []
        encontrado = False # fix: verifica si existe
        for i in self.jugadores:
            if i.dorsal != dorsal:
                aux += [i]
            else:
                gestion_archivos("elim", "jugadores.txt", f"{self.pais.codigo_fifa},{i.linea()}", None)
                encontrado = True
        if not encontrado:
            return "Jugador no encontrado." # fix: retorna str para messagebox
        self.jugadores = aux

    #E:dorsal
    #S:el jugador encontrado o nada
    #R:ninguna
    #objetivo:buscar un jugador de la seleccion por su dorsal
    def buscar_jugador(self, dorsal):
        for j in self.jugadores:
            if j.dorsal == dorsal:
                return j
        return None # fix: retorna None si no existe, se verifica en la interfaz

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:eliminar la seleccion de la lista y del archivo
    def eliminar(self):
        global selecciones
        aux = []
        for s in selecciones:
            if s.pais.codigo_fifa != self.pais.codigo_fifa:
                aux += [s]
        selecciones = aux
        gestion_archivos("elim", "selecciones.txt", f"{self.pais.codigo_fifa}", None)

    #E:codigo del pais
    #S:la seleccion encontrada o nada
    #R:ninguna
    #objetivo:buscar una seleccion por el codigo de su pais
    def buscar(codigo_pais):
        for s in selecciones:
            if s.pais.codigo_fifa == codigo_pais:
                return s
        return None # fix: retorna None si no existe, se verifica en la interfaz

    #E:entrenador
    #S:mensaje de error si el entrenador no es valido
    #R:ninguna
    #objetivo:asignar un nuevo entrenador a la seleccion
    def asignar_entrenador(self, entrenador):
        if not isinstance(entrenador, Entrenador):
            return "El entrenador no es valido." # fix: mensaje mas claro
        linea_vieja = self.linea()
        self.entrenador = entrenador
        gestion_archivos("act", "selecciones.txt", linea_vieja, self.linea())

    #E:ninguna
    #S:la fuerza del equipo o mensaje de error
    #R:la seleccion debe tener al menos 11 jugadores
    #objetivo:calcular la fuerza del equipo
    def calcular_fuerza_equipo(self):
        if len(self.jugadores) < 11: # fix: verifica minimo antes de calcular
            return "Se necesitan al menos 11 jugadores para calcular la fuerza."
        try:
            self.fuerza_equipo = Validaciones().fuerza_equipo_def(Validaciones().onceGrandes(self.jugadores), self.entrenador, self.pais)
            return self.fuerza_equipo
        except Exception as e: # fix: muestra el error real en vez de mensaje generico
            return f"Error al calcular fuerza: {e}"

    #E:goles a favor, goles en contra, tarjetas amarillas, tarjetas rojas
    #S:mensaje de error si algun dato es invalido
    #R:cada dato debe ser mayor o igual a 0
    #objetivo:sumar el resultado de un partido a las estadisticas de la seleccion
    def registrar_resultado(self, goles_favor, goles_contra, tarjetas_am, tarjetas_roj):
        linea_vieja = self.linea()
        if not isinstance(goles_favor, int) or goles_favor < 0:
            return "El total de goles a favor debe ser un número entero mayor o igual a 0."
        else:
            self.total_goles_favor += goles_favor
        if not isinstance(goles_contra, int) or goles_contra < 0:
            return "El total de goles en contra debe ser un número entero mayor o igual a 0."
        else:
            self.total_goles_contra += goles_contra
        if not isinstance(tarjetas_am, int) or tarjetas_am < 0:
            return "El total de tarjetas amarillas debe ser un número entero mayor o igual a 0."
        else:
            self.total_tarjetas_amarillas += tarjetas_am
        if not isinstance(tarjetas_roj, int) or tarjetas_roj < 0:
            return "El total de tarjetas rojas debe ser un número entero mayor o igual a 0."
        else:
            self.tarjetas_roj += tarjetas_roj
        gestion_archivos("act", "selecciones.txt", linea_vieja, self.linea())
#Emanuel (arriba)

            
        
# -----------------------------------------------------------------------------------
#Kerry
class Partido:

    #E:id del partido, equipo1, equipo2, fase, fecha
    #S:instancia del partido
    #R:ninguna
    #objetivo:crear un partido entre dos equipos
    def __init__(self,id_partido, equipo1, equipo2, fase, fecha):
        if not Validaciones().debeser(id_partido, int):
            print(Validaciones().debeser(id_partido,int))
            return
        else:
            self.id = id_partido
            
        if not Validaciones().debeser(equipo1, str):
            print(Validaciones().debeser(equipo1,str))
            return
        else:
            self.equipo1 = equipo1
        if not Validaciones().debeser(equipo2, str):
            print(Validaciones().debeser(equipo2, str)) 
            return
        else:
            self.equipo2 = equipo2
        if not Validaciones().debeser(fase, str):
            print(Validaciones().debeser(fase,str))
            return
        else:
            self.fase = fase         
        if not Validaciones().debeser(fecha, str):
            print(Validaciones().debeser(fecha, str))
            return
        else:
            self.fecha = fecha
            
        self.mundial = "Mundial FIFA 2026"
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.ganador = ""

    #E:equipo1, equipo2
    #S:ninguna
    #R:ninguna
    #objetivo:resolver un empate por penales y definir el ganador
    def Desempate(self, equipo1, equipo2):

            self.penales1 = 0
            self.penales2 = 0
            while self.penales1 == self.penales2:
                self.penales1 = random.randint(0, 5)
                self.penales2 = random.randint(0, 5)
                
            if self.penales1 > self.penales2:
                self.ganador = equipo1
            else:
                self.ganador = equipo2

    #E:ninguna
    #S:ninguna
    #R:ambas selecciones deben existir
    #objetivo:simular los goles del partido entre las dos selecciones
    def simular(self):
        equipo1 = None
        equipo2 = None
        for seleccion in selecciones:
            if seleccion.pais.nombre == self.equipo1:
                equipo1 = seleccion
            if seleccion.pais.nombre == self.equipo2:
                equipo2 = seleccion
                
        if equipo1 == None or equipo2 == None:
            print(f"No se encontraron las selecciones para el partido: {self.equipo1} vs {self.equipo2}")
            return
        self.fuerza1 = equipo1.calcular_fuerza_equipo()
        self.fuerza2 = equipo2.calcular_fuerza_equipo()
        
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

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:definir el ganador del partido segun los goles
    def generar_ganadores(self):
        if self.goles_equipo1 == self.goles_equipo2:
            if self.fase != grupos:
                 self.Desempate(self.equipo1, self.equipo2)
            else:
                self.ganador = "Empate"
                print (f"Empate entre {self.equipo1} y {self.equipo2}  ")
        else:
            if self.goles_equipo1 > self.goles_equipo2:
                self.ganador = self.equipo1
                self.golestotal = self.goles_equipo1
            else:
                self.ganador = self.equipo2
                self.golestotal = self.goles_equipo2
        
            print (f"Ganador del partido: {self.ganador} con {self.golestotal} goles")

    #E:ninguna
    #S:el resultado del partido en texto
    #R:ninguna
    #objetivo:mostrar el resultado del partido
    def mostrar_resultados(self):
        return f"{self.equipo1} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo2}"

class Grupo:
    #E:nombre del grupo
    #S:instancia del grupo
    #R:ninguna
    #objetivo:crear un grupo de la fase de grupos
    def __init__(self, nombre_grupo):
        if not Validaciones().debeser(nombre_grupo, str):
            print(Validaciones().debeser(nombre_grupo, str))
            return
        else:
            self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []


    #E:seleccion, fuerza
    #S:ninguna
    #R:el grupo no debe tener mas de 4 equipos
    #objetivo:agregar un equipo al grupo
    def agregar_equipo(self, seleccion, fuerza):
        if len(self.equipos) >= 4:
            print("No se pueden agregar más equipos al grupo.")
            return
        if not Validaciones().debeser(seleccion, Seleccion):
            print(Validaciones().debeser(seleccion, Seleccion))
            return
        else:
            self.equipos += [[seleccion,fuerza]]

    #E:ninguna
    #S:mensaje si el grupo esta incompleto
    #R:el grupo debe tener 4 equipos
    #objetivo:simular todos los partidos del grupo
    def jugar_partidos(self):
        if len(self.equipos) != 4:
            return "No se puede empezar los partidos porque el grupo esta incompleto"
        
        else:   
            for Equipo1 in range(len(self.equipos)):
                for Equipo2 in range(Equipo1 + 1, len(self.equipos)):
                    nombre1 = self.equipos[Equipo1][0].pais.nombre
                    nombre2 = self.equipos[Equipo2][0].pais.nombre
                    partido = Partido(len(self.partidos) +1, nombre1, nombre2, self.nombre_grupo, "20/06/2026")
              
                    partido.simular()
                    partido.generar_ganadores()
                    self.partidos += [partido] 
                    
                    gestion_archivos("agg", "partidos.txt",f"{partido.id},{partido.equipo1},{partido.equipo2},{partido.fase},{partido.fecha},{partido.goles_equipo1},{partido.goles_equipo2},{partido.ganador},", None )

                    print (partido.mostrar_resultados())

    #E:ninguna
    #S:la tabla del grupo
    #R:ninguna
    #objetivo:calcular la tabla de posiciones del grupo
    def calcular_tabla(self): #Nombre, goles a favor, goles en contra, diferencia de goles, puntos
        tabla = []
        for equipo in self.equipos:
            seleccion = equipo[0]
            nombre_equipo = seleccion.pais.nombre
            tabla += [[nombre_equipo, 0, 0, 0 ,0]]
        
        for partido in self.partidos:
            ego1 = None
            ego2 = None
            for i in range(len(tabla)):
                if tabla[i][0] == partido.equipo1:
                    ego1 = i
                if tabla[i][0] == partido.equipo2:
                    ego2 = i
                    
            tabla[ego1][1] += partido.goles_equipo1
            tabla[ego1][2] += partido.goles_equipo2
            tabla[ego2][1] += partido.goles_equipo2
            tabla[ego2][2] += partido.goles_equipo1
            
            tabla[ego1][3] = tabla[ego1][1] - tabla[ego1][2]
            tabla[ego2][3] = tabla[ego2][1] - tabla[ego2][2]
            
            if partido.ganador == "Empate":
                tabla[ego1][4] += 1
                tabla[ego2][4] += 1
            elif partido.ganador == partido.equipo1:
                tabla[ego1][4] += 3
            else:
                tabla[ego2][4] += 3
                
        
        return tabla

    #E:ninguna
    #S:los dos equipos clasificados del grupo
    #R:ninguna
    #objetivo:obtener los equipos que clasifican del grupo
    def obtener_clasificados(self):
        tabla = self.calcular_tabla()
        clasificados = []
        tabla_aux = []
        clasificado1 = 0
        clasificado2 = None
        
        for equipo in range(1, len(tabla)):
            if tabla[equipo][4] > tabla[clasificado1][4]:
                clasificado1 = equipo
            elif tabla[equipo][4] == tabla[clasificado1][4]:
                if tabla[equipo][3] > tabla[clasificado1][3]:
                    clasificado1 = equipo 
        clasificados += [tabla[clasificado1][0]]
        tabla_aux += [tabla[clasificado1][0]]
        
        for equipo in range(len(tabla)):
            encontrado = False
            for nombre in tabla_aux:
                if tabla[equipo][0] == nombre:
                    encontrado = True
                
            if not encontrado:
                if clasificado2 == None:
                    clasificado2 = equipo
                elif tabla[equipo][4] > tabla[clasificado2][4]:
                    clasificado2 = equipo
                elif tabla[equipo][4] == tabla[clasificado2][4]:
                    if tabla[equipo][3] > tabla[clasificado2][3]:
                        clasificado2 = equipo
        clasificados += [tabla[clasificado2][0]]
        
        return clasificados

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar la tabla del grupo
    def mostrar_tabla(self):
        tabla = self.calcular_tabla()
        print(f"Tabla del Grupo {self.nombre_grupo}")
        print("Equipo | GF | GC | DG | P")
        for fila in tabla:
            print(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}")
     
class Fase:
    #E:fase
    #S:instancia de la fase
    #R:la fase debe ser una de las existentes
    #objetivo:crear una fase eliminatoria
    def __init__(self, fase):
        if not Validaciones().debeser(fase, str):
            print(Validaciones().debeser(fase, str))
            return
        else:
            if not Validaciones().fase_valida(fase):
                print(Validaciones().fase_valida(fase))
            else:
                self.fase = fase
        self.partidos = []

    #E:equipo1, equipo2
    #S:ninguna
    #R:ninguna
    #objetivo:agregar un partido a la fase
    def agregar_partido(self, equipo1, equipo2):
        id_partido = len(self.partidos) + 1
        partido = Partido(id_partido, equipo1, equipo2, self.fase, "20/06/2026")
        self.partidos += [partido]

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:simular todos los partidos de la fase
    def jugar_partidos(self):
        for partido in self.partidos:
            partido.simular()
            partido.generar_ganadores()
            print(partido.mostrar_resultados())

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar los partidos de la fase
    def mostrar_juegos(self):
        for partido in self.partidos:
            print(f"Partido: {partido.equipo1} vs {partido.equipo2}")
            print(f"Goles: {partido.goles_equipo1} - {partido.goles_equipo2}")
            print(f"Ganador: {partido.ganador}")
            print(f"Fecha: {partido.fecha}")

    #E:ninguna
    #S:los ganadores de la fase
    #R:ninguna
    #objetivo:obtener los equipos que ganaron en la fase
    def obtener_clasificados(self):
        ganadores = []
        for partido in self.partidos:
            ganadores += [partido.ganador]
        return ganadores
    
class Mundial:
    #E:nombre, año
    #S:instancia del mundial
    #R:el año debe estar entre 1900 y 2026
    #objetivo:crear el mundial con su nombre y año
    def  __init__(self, nombre, año):
        if not Validaciones().debeser(nombre, str):
            print(Validaciones().debeser(nombre, str))
            return
        else:
            self.nombre = nombre
        if not Validaciones().debeser(año, int) or año < 1900 or año > 2026:
            print(Validaciones().debeser(año, int))
            return
        else:
            self.año = año
        self.paises = []
        self.selecciones = []
        self.grupos = []
        self.fases = []
        self.campeon = None

    #E:codigo fifa, nombre, continente, ranking fifa
    #S:ninguna
    #R:ninguna
    #objetivo:agregar un pais al mundial
    def agregar_pais(self, codigo_fifa, nombre, continente, ranking_fifa ):
        pais = Pais(codigo_fifa,nombre,continente,ranking_fifa, True)
        self.paises += [pais]

    #E:pais, entrenador
    #S:ninguna
    #R:ninguna
    #objetivo:registrar una seleccion en el mundial
    def registrar_seleccion(self, pais, entrenador):
        global selecciones
        seleccion = Seleccion(pais, entrenador, True)
        self.selecciones += [seleccion]
        selecciones += [seleccion]

    #E:cantidad de grupos
    #S:ninguna
    #R:la cantidad de selecciones debe dividirse en grupos de 4 equipos
    #objetivo:crear los grupos del mundial con las selecciones registradas
    def crear_grupos(self, cantidad_grupos):
        if not Validaciones().debeser(cantidad_grupos, int) or cantidad_grupos <= 0:
            print(Validaciones().debeser(cantidad_grupos,int))
            return
            
        elif cantidad_grupos > len(grupos):
            print(f"No se pueden crear {cantidad_grupos} grupos. El número máximo de grupos es {len(grupos)}.")
            return
        elif len(self.selecciones) / cantidad_grupos != 4:
            print("El número de grupos debe ser tal que cada grupo tenga 4 equipos.")   
            return
        else:
            
          
            
            for i in range(cantidad_grupos):
            
                nombre_grupo = grupos[i]
                grupo = Grupo(nombre_grupo)
                
                for seleccion in range(4):
                    seleccion_actual = self.selecciones[i * 4 + seleccion]
                    fuerza_equipo = seleccion_actual.calcular_fuerza_equipo()
                    if isinstance(fuerza_equipo, str):
                        print(f"Error:{fuerza_equipo}")
                        return
                    grupo.agregar_equipo(seleccion_actual, fuerza_equipo)
        
                self.grupos += [grupo]

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:simular la fase de grupos y guardar el ranking
    def jugar_fase_grupos(self):
        for grupo in self.grupos:
            grupo.jugar_partidos()
            grupo.mostrar_tabla()
            print(f"Equipos clasificados del {grupo.nombre_grupo}: {grupo.obtener_clasificados()}")
        self.guardar_ranking()

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:armar la primera fase eliminatoria con los clasificados de los grupos
    def armar_fase_eliminatoria(self):
        fases = ["dieciseisavos", "octavos", "cuartos", "semifinales", "final"]
        fase_actual = fases[0]
        
        fase_eliminatoria = Fase(fase_actual)
        
        for grupo in range(0, len(self.grupos), 2):
            grupo_actual = self.grupos[grupo]
            grupo_siguiente = self.grupos[grupo + 1]
            clasificados_A = grupo_actual.obtener_clasificados()
            clasificados_B = grupo_siguiente.obtener_clasificados()
            
            cruces = [(clasificados_A[0], clasificados_B[1]), (clasificados_A[1], clasificados_B[0])]
    
            for nome1, nome2 in cruces:
                fase_eliminatoria.agregar_partido(nome1, nome2)
                
        self.fases += [fase_eliminatoria]

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:simular todas las fases eliminatorias
    def jugar_fase_eliminatoria(self):
        for fase in self.fases:
            fase.jugar_partidos()
            fase.mostrar_juegos()
            clasificados = fase.obtener_clasificados()
            print(f"Equipos clasificados de la {fase.fase}: {clasificados}")

    #E:ninguna
    #S:ninguna
    #R:debe existir al menos una fase con partidos jugados
    #objetivo:determinar el campeon del mundial
    def determinar_campeon(self):
        if len(self.fases) > 0:
            ultima_fase = self.fases[-1]
            if len(ultima_fase.partidos) > 0:
                ultimo_partido = ultima_fase.partidos[-1]
                self.campeon = ultimo_partido.ganador
                print(f"El campeón del Mundial {self.nombre} {self.año} es: {self.campeon}")
            else:
                print("No se han jugado partidos en la última fase.")
                return
        else:
            print("No se ha jugado ningun partido")

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:mostrar la tabla general de todos los grupos
    def mostrar_tabla_general(self):
        possicion = 1
        print(f"Tabla General del Mundial {self.nombre} {self.año}")
        print("Posicion | Equipo | GF| GC | DG | Puntos")
        for grupo in self.grupos:
            tabla = grupo.calcular_tabla()
            for fila in tabla:
                print(f"{possicion} | {fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}")
                possicion += 1

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:generar un reporte del mundial en un archivo
    def generar_reportes(self):
        archivo = open("reporte.txt", "w", encoding="utf-8")
        archivo.write(f"Resumen del Mundial {self.nombre} {self.año}\n")
        archivo.write("Equipos:\n")
        for seleccion in self.selecciones:
            archivo.write(f"{seleccion.pais.nombre} - Entrenador: {seleccion.entrenador.nombre} {seleccion.entrenador.apellido}\n")
            archivo.write("Jugadores:\n")
            for jugador in seleccion.jugadores:
                archivo.write(f"{jugador.nombre} {jugador.apellido} - Posición: {jugador.posicion}, Goles: {jugador.goles}, Asistencias: {jugador.asistencias}, Puntaje: {jugador.puntaje_individual}\n")
        archivo.write("\nResultados de la fase de grupos:\n")
        for grupo in self.grupos:
            archivo.write(f"{grupo.nombre_grupo}:\n")
            for partido in grupo.partidos:
                archivo.write(f"{partido.equipo1} {partido.goles_equipo1} - {partido.goles_equipo2} {partido.equipo2} | Ganador: {partido.ganador}\n")
        archivo.write("\nResultados de la fase eliminatoria:\n")
        for fase in self.fases:
            archivo.write(f"{fase.fase}:\n")
            for partido in fase.partidos:
                archivo.write(f"{partido.equipo1} {partido.goles_equipo1} - {partido.goles_equipo2} {partido.equipo2} | Ganador: {partido.ganador}\n")
        archivo.write(f"\nCampeón: {self.campeon}\n")
                
        archivo.close()

    #E:ninguna
    #S:ninguna
    #R:ninguna
    #objetivo:guardar el ranking de selecciones en un archivo
    def guardar_ranking(self):
        posicion = 1
        ranking = ""
        for grupo in self.grupos:
            tabla = grupo.calcular_tabla()
            for fila in tabla:
                ranking += f"{posicion},{fila[0]},{fila[1]},{fila[2]},{fila[3]},{fila[4]}\n"
                posicion += 1
                
        archivo = open("ranking_selecciones.txt", "w", encoding="utf-8")
        archivo.write(ranking)
        archivo.close()
            


#despues de esta funcion poner todo lo de tk
#E:ninguna
#S:ninguna
#R:los archivos deben existir para cargar datos
#objetivo:cargar paises entrenadores selecciones y jugadores desde los archivos
def cargar_todo():
   
    global paises
    global entrenadores
    global selecciones
    
    #Paises
    try:
        archivo = open("paises.txt", "r")
        for linea in archivo.readlines():
            datos = linea.strip().split(",")
            paises += [Pais(datos[0], datos[1], datos[2], int(datos[3]))]
        archivo.close()
    except FileNotFoundError:
        pass

    #Entrenadores
    try:
        archivo = open("entrenadores.txt", "r")
        for linea in archivo.readlines():
            datos = linea.strip().split(",")
            entrenadores += [(datos[0], Entrenador(datos[1], datos[2], datos[3], datos[4], datos[5], int(datos[6]), datos[7]))]
        archivo.close()
    except FileNotFoundError:
        pass

    #Selecciones
    try:
        archivo = open("selecciones.txt", "r")
        for linea in archivo.readlines():
            datos = linea.strip().split(",")
            for p in paises:
                if p.codigo_fifa == datos[0]:
                    for codigo, entrenador in entrenadores:
                        if codigo == datos[0]:
                            selecciones += [Seleccion(p, entrenador)]
        archivo.close()
    except FileNotFoundError:
        pass

    #Jugadores
    try:
        archivo = open("jugadores.txt", "r")
        for linea in archivo.readlines():
            datos = linea.strip().split(",")
            codigo_pais = datos[0]
            jugador = Futbolista(datos[1], datos[2], datos[3], datos[4], int(datos[5]), datos[6], int(datos[7]), int(datos[8]), int(datos[9]), int(datos[10]), int(datos[11]))
            for seleccion in selecciones:
                if seleccion.pais.codigo_fifa == codigo_pais:
                    seleccion.jugadores += [jugador]
        archivo.close()
    except FileNotFoundError:
        pass




######################################################################################################################################################
#Interfaz de usuario
mundial = Mundial("Mundial FIFA 2026", 2026)
cargar_todo()
mundial.selecciones = selecciones

ventana_principal = tk.Tk()
ventana_principal.geometry("900x600")
ventana_principal.resizable(False, False)
ventana_principal.title("Mundial FIFA 2026")

imagen = Image.open("fondo.jpeg").resize((900, 600), Image.LANCZOS)
foto = ImageTk.PhotoImage(imagen)
canvas = tk.Canvas(ventana_principal, width=900, height=600, bd=0, highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, anchor="nw", image=foto)
canvas.image = foto

zona_paises = canvas.create_rectangle(20, 171, 489, 231, outline="", fill="")
canvas.tag_bind(zona_paises, "<Button-1>", lambda e: tk.messagebox.showinfo("Prueba", "Botón 1 funcionando"))

zona_jugadores = canvas.create_rectangle(20, 250, 489, 310, outline="", fill="")
canvas.tag_bind(zona_jugadores, "<Button-1>", lambda e: tk.messagebox.showinfo("Prueba", "Botón 2 funcionando"))

zona_config = canvas.create_rectangle(20, 330, 489, 390, outline="", fill="")
canvas.tag_bind(zona_config, "<Button-1>", lambda e: configurar_mundial())

zona_jugar = canvas.create_rectangle(20, 410, 489, 470, outline="", fill="")
canvas.tag_bind(zona_jugar, "<Button-1>", lambda e: menu_jugar())

zona_stats = canvas.create_rectangle(20,490, 489, 550, outline="", fill="")
canvas.tag_bind(zona_stats, "<Button-1>", lambda e: tk.messagebox.showinfo("Prueba", "Botón 5 funcionando"))

#E:ninguna
#S:ninguna
#R:ninguna
#objetivo:abrir la ventana de configuracion del mundial
def configurar_mundial():
    ventana = tk.Toplevel(ventana_principal)
    ventana.title("Configuracion del Mundial")
    ventana.geometry("600x400")
    ventana.resizable(False, False)
    
    imagen = Image.open("fondo_config.png").resize((600, 400), Image.LANCZOS)
    foto = ImageTk.PhotoImage(imagen)
    canva = tk.Canvas(ventana, width=600, height=400, bd=0,highlightthickness=0)
    canva.pack(fill="both", expand=True)
    canva.create_image(0,0, anchor="nw", image=foto)
    ventana.image = foto
    
    btn1 = tk.Button(ventana, text="Crear Grupos", width=20, font=("Arial", 11), command=crear_grupos)
    canva.create_window(300,160, window=btn1)
    
    btn2 = tk.Button(ventana, text="Ver Grupos", width=20, font=("Arial", 11), command=ver_grupos)
    canva.create_window(300,230, window=btn2)
    
    btn3 = tk.Button(ventana, text="Regresar al Menu", width=20, font=("Arial", 11), command=ventana.destroy)
    canva.create_window(300,300, window=btn3)

#E:ninguna
#S:ninguna
#R:ninguna
#objetivo:abrir la ventana para ingresar la cantidad de grupos y crearlos
def crear_grupos():
    ventana_grupos = tk.Toplevel(ventana_principal)
    ventana_grupos.geometry("400x250")
    ventana_grupos.resizable(False, False)
    ventana_grupos.configure(bg="#2c3e50")

    ventana_grupos.grab_set()

    lbl_intruccion = tk.Label(ventana_grupos, text="Ingrese la cantidad de grupos:", font=("Arial", 12, "bold"), bg="#2c3e50", fg="white")
    lbl_intruccion.pack(pady=20)

    cantidad= tk.Entry(ventana_grupos, font=("Arial", 12), justify="center", width=10)
    cantidad.pack(pady=10)
    cantidad.focus()

    #E:ninguna
    #S:ninguna
    #R:la cantidad de selecciones debe dividirse en grupos de 4 equipos
    #objetivo:confirmar la creacion de los grupos con la cantidad ingresada
    def confirmar():
        valor = cantidad.get()
        num_grupos = int(valor)


        if num_grupos > len(grupos):
            tk.messagebox.showerror("Error", f"El numero maximo de grupos es {len(grupos)}")
            return
        if len(selecciones) == 0:
            tk.messagebox.showwarning("Aviso", "No hay selecciones registradas en el sistema")

        if len(selecciones) / num_grupos != 4:
            tk.messagebox.showerror("Error",f"La cantidad de selecciones no se pueden dividir equitativamente")
            return
        mundial.crear_grupos(num_grupos)
        tk.messagebox.showinfo("Exito","Grupos creados con exito")
        ventana_grupos.destroy()


    btn_aceptar = tk.Button(ventana_grupos, text="Aceptar", font=("Arial", 11, "bold"), width=15, command=confirmar)
    btn_aceptar.pack(pady=20)

#E:ninguna
#S:ninguna
#R:los grupos deben estar creados
#objetivo:mostrar la distribucion de los grupos del mundial
def ver_grupos():
    if len(mundial.grupos) == 0:
        tk.messagebox.showwarning("Aviso", "Primero debe crear los grupos en el sistema")
        return
    ventana_ver = tk.Toplevel(ventana_principal)
    ventana_ver.title("Grupos del Mundial")
    ventana_ver.geometry("600x500")
    ventana_ver.resizable(False, False)

    imagen = Image.open("fondo_config.png").resize((600,500), Image.LANCZOS)
    foto = ImageTk.PhotoImage(imagen)
    canva = tk.Canvas(ventana_ver, width=600, height=500, bd=0, highlightthickness=0)
    canva.pack(fill="both", expand=True)
    canva.create_image(0, 0, anchor="nw", image=foto)
    ventana_ver.image = foto

    canva.create_text(300, 40, text="Distribucion de grupos", font=("Arial", 16, "bold"), fill="white")
    txt_area = scrolledtext.ScrolledText(ventana_ver, width=55, height=18, font=("Courier New", 11), bg="#1a252f", fg="white", bd=2)
    canva.create_window(300, 240, window=txt_area)

    grupostxt = ""
    for grupo in mundial.grupos:
        grupostxt += f"==={grupo.nombre_grupo}===\n"

        for equipo in grupo.equipos:
            seleccion = equipo[0]
            pais_nombre = seleccion.pais.nombre
            grupostxt += f" >{pais_nombre}\n"
        grupostxt += "\n"
    txt_area.insert(tk.END, grupostxt)
    txt_area.configure(state="disable")

    btn_regresar = tk.Button(ventana_ver, text="Regresar", width=15, font=("Arial", 11, "bold"), command=ventana_ver.destroy)
    canva.create_window(300, 440, window=btn_regresar)
    

#E:ninguna
#S:ninguna
#R:ninguna
#objetivo:abrir el menu para jugar el mundial
def menu_jugar():
    ventana = tk.Toplevel(ventana_principal)
    ventana.title("Jugar Mundial")
    ventana.geometry("600x400")
    ventana.resizable(False, False)

    imagen = Image.open("fondo_jugar.png").resize((600, 400), Image.LANCZOS)
    foto = ImageTk.PhotoImage(imagen)
    canva = tk.Canvas(ventana, width=600, height=400, bd=0, highlightthickness=0)
    canva.pack(fill="both", expand=True)
    canva.create_image(0,0, anchor="nw", image=foto)
    ventana.image = foto

    btn1 = tk.Button(ventana, text="Simular fase", width=20, font=("Arial", 11), command=Simular_fase)
    canva.create_window(300,160, window=btn1)

    btn2 = tk.Button(ventana, text="Avanzar a siguiente fase", width=20, font=("Arial", 11), command=Avanzar_fase)
    canva.create_window(300,230, window=btn2)

    btn3 = tk.Button(ventana, text="Regresar al Menu", width=20, font=("Arial", 11), command=ventana.destroy)
    canva.create_window(300,300, window=btn3)

#E:ninguna
#S:ninguna
#R:los grupos deben estar creados
#objetivo:simular la fase de grupos o la fase eliminatoria actual y mostrar el resultado
def Simular_fase():
    if len(mundial.grupos) == 0:
        tk.messagebox.showwarning("Aviso", "Primero debe crear los grupos")
        return
    if len(mundial.fases) == 0:
        mundial.jugar_fase_grupos()
        reporte = "Resultados: Fase de Grupos"

        resumen = ""
        for grupo in mundial.grupos:
            resumen +=f"=== Tabla {grupo.nombre_grupo} === \n"
            tabla = grupo.calcular_tabla()
            for fila in tabla:
                resumen += f"Equipo: {fila[0]} | GF: {fila[1]} | GC: {fila[2]} | {fila[3]} | Pts: {fila[4]}\n"
            resumen += "\n"
    else:
        fase_actual = mundial.fases[-1]

        if len(fase_actual.partidos) > 0 and fase_actual.partidos[0].ganador != "":
            tk.messagebox.showinfo("Aviso", "Esta fase ya ha sido simulada")
            return

        fase_actual.jugar_partidos()
        reporte = f"Resultado: Fase {fase_actual.fase.capitalize()}"

        for partido in fase_actual.partidos:
            linea_partido = f"{partido.id},{partido.equipo1},{partido.equipo2},{partido.fase},{partido.fecha},{partido.goles_equipo1},{partido.goles_equipo2},{partido.ganador}"
            gestion_archivos("agg", "partidos.txt", linea_partido, None)

        resumen = f"===Encuentro de {fase_actual.fase} === \n\n"
        for partido in fase_actual.partidos:
            resumen += f"{partido.equipo1} ({partido.goles_equipo1}) vs {partido.equipo2} ({partido.goles_equipo2})\n"
            resumen += f"Ganador: {partido.ganador}\n\n"

        if fase_actual.fase.lower() == "final":
            mundial.determinar_campeon()
            resumen += f"EL CAMPEON DEL MUNDIAL ES {mundial.campeon}\n"

    ventana_res = tk.Toplevel(ventana_principal)
    ventana_res.title(reporte)
    ventana_res.geometry("550x450")
    ventana_res.resizable(False, False)
    ventana_res.configure(bg="#2c3e50")
    ventana_res.grab_set()

    lbl_fase = tk.Label(ventana_res, text=reporte, font=("Arial", 14, "bold"), bg="#2c3e50", fg="white")
    lbl_fase.pack(pady=15)

    txt_area = scrolledtext.ScrolledText(ventana_res, width=60, height=16, font=("Arial", 10, "bold"), bg="#1a252f", fg="white", bd=2)
    txt_area.pack(pady=5)
    txt_area.insert(tk.END, resumen)
    txt_area.configure(state="disabled")

    btn_ok = tk.Button(ventana_res, text="Aceptar", width=15, font=("Arial", 11, "bold"), command=ventana_res.destroy) 
    btn_ok.pack(pady=15)

#E:ninguna
#S:ninguna
#R:los grupos deben estar creados y la fase de grupos simulada
#objetivo:avanzar a la siguiente fase del mundial
def Avanzar_fase():
    if len(mundial.grupos) == 0:
        tk.messagebox.showwarning("Aviso", "No se puede avanzar si no se han creado los grupos")
        return
    if len(mundial.fases) == 0:
        if len(mundial.grupos[0].partidos) == 0:
            tk.messagebox.showwarning("Aviso", "Primero debe simular la fase de grupos")
            return
        mundial.armar_fase_eliminatoria()
        fase_nueva = mundial.fases[-1].fase
        tk.messagebox.showinfo("Avance de Fase", "Fase de grupos terminada")

    else:
        fase_anterior = mundial.fase[-1]

        if len(fase_anterior.partidos) == 0 or fase_anterior.partidos[0].ganador == "":
            tk.messagebox.showwarning("Aviso", "Debe simular los partidos actuales antes de avanzar")
            return
        if fase_anterior.fase.lower() == "final":
            tk.messagebox.showinfo("Final del torneo", f"El mundial ha concluido. El campeon es {mundial.campeon}")

        lista_orden = ["dieciseisavos", "octavos", "cuartos", "semifinales", "final"]
        iden_actual = lista_orden.index(fase_anterior.fase.lower())
        nombre_siguiente = lista_orden[iden_actual + 1]

        














