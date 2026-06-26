import random
#Notas:
#validar si jugador ya existe en otra seleccion
#
#Validacionesy funciones

grupos = ["Grupo A", "Grupo B", "Grupo C", "Grupo D", "Grupo E", "Grupo F", "Grupo G", "Grupo H", "Grupo I", "Grupo J", "Grupo K", "Grupo L",]

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
    def onceGrandes(self,lista):
        for i in range(len(lista)):
            for j in range(len(lista)):
                if lista[i].puntaje_individual > lista[j].puntaje_individual:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        return lista[0:11]
    def fuerza_equipo_def(self,jugadores,entrenador,pais): #jugadores con OnceGrandes()
        
        fuerza_equipo=0
        for jugador in jugadores:
            fuerza_equipo += jugador.puntaje_individual
        fuerza_equipo = (fuerza_equipo / 11)*0.6
        if entrenador.experiencia_anios*4>100:
            factor_entrenador= 100
        else:
            factor_entrenador=entrenador.experiencia_anios*4
        fuerza_equipo+=factor_entrenador*0.25
        fuerza_equipo+=(100-pais.ranking_fifa)*0.15    
        return fuerza_equipo


    def fase_valida(self,fase):
        fases_validas = [grupos,"dieciseisavos", "octavos", "cuartos", "semifinales", "final"]
        if not fase.lower() in fases_validas: 
            return "La fase debe ser una existente"
        return True
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
        else:
            if Validaciones().SinEspacios(continente) != True:
                raise ValueError("El continente no debe iniciar o terminar  con espacios.")
            else:
                self.continente = continente
        if not isinstance(ranking_fifa,int):
            raise ValueError("El rank FIFA debe ser un numero")
        self.ranking_fifa = ranking_fifa
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
    def __init__(self,dorsal,posicion, total_tarjetas_amarillas, tarjetas_roj, goles,asistencias,puntaje_individual):
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
        print(f"Total Tarjetas Rojas: {self.tarjetas_roj}")
        print(f"Goles: {self.goles}")
        print(f"Asistencias: {self.asistencias}")
        print(f"Puntaje Individual: {self.puntaje_individual}")
    def actualizar_datos(self, dorsal, posicion, total_tarjetas_amarillas, tarjetas_roj, goles, asistencias, puntaje_individual):
        
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
        if isinstance(tarjetas_roj, int) and tarjetas_roj >= 0 and tarjetas_roj!=None:
            self.tarjetas_roj = tarjetas_roj
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
            if (puntaje_individual).lower()!="original":
                if isinstance(puntaje_individual, int) and puntaje_individual > 0 and puntaje_individual <= 100:
                    self.puntaje_individual = puntaje_individual
                else:
                    raise ValueError("El puntaje individual debe ser un número entero entre 0 y 100.")
    def registrar_gol(self):
        self.goles += 1
    def registrar_asistencia(self):
        self.asistencias += 1
    def registrar_tarjeta(self, tipo):
        if tipo.lower() == "amarilla":
            self.total_tarjetas_amarillas += 1
        elif tipo.lower() == "roja":
            self.tarjetas_roj += 1
        else:
            print("Tipo de tarjeta inválido. Debe ser amarilla o roja.")
    def dorsal(self):
        print(self.dorsal)
class Seleccion:

    codigo_equipo=0
    def __init__(self,pais,entrenador): #,jugadores,goles_favor,goles_contra,total_tarjetas_amarillas,tarjetas_roj
        
        if not isinstance(pais,object) or not isinstance(entrenador,object):
           raise ValueError("El país y entrenador deben ser objetos válidos.") 
        else:
            self.pais = pais
        if not isinstance(entrenador,Entrenador):
            raise ValueError("El entrenador ingresado no existe")
        else:
            self.entrenador = entrenador
        """
        if not isinstance(goles_favor, int) or goles_favor < 0:
            raise ValueError("El total de goles a favor debe ser un número entero mayor o igual a 0.")
        else:
            self.goles_favor = goles_favor
        if not isinstance(goles_contra, int) or goles_contra < 0:
            raise ValueError("El total de goles en contra debe ser un número entero mayor o igual a 0.")
        else:
            self.goles_contra = goles_contra
        if not isinstance(total_tarjetas_amarillas, int) or total_tarjetas_amarillas < 0:
            raise ValueError("El total de tarjetas amarillas debe ser un número entero mayor o igual a 0.")
        else:
            self.total_tarjetas_amarillas = total_tarjetas_amarillas
        if not isinstance(tarjetas_roj, int) or tarjetas_roj < 0:
            raise ValueError("El total de tarjetas rojas debe ser un número entero mayor o igual a 0.")
        else:
            self.tarjetas_roj = tarjetas_roj
        if isinstance(jugadores,list):
            if not len(jugadores)>=11 and len(jugadores)<=23:
                raise ValueError("El tamaño de el equipo noo es permitido.")
            for i in jugadores:
                if isinstance(i,object):
                    for jugador in jugadores:
                        for jugadorComparar in jugadores:
                            if jugador==jugadorComparar:
                                raise ValueError("Los jugadores no pueden estar repetidos.")

                else:
                    raise ValueError("Lista de jugadores debe ser de objetos.")
        raise ValueError("Los jugadores deben estar en una lista.")
        """
        self.jugadores=[]
        self.goles_favor=0
        self.goles_contra = 0
        self.total_tarjetas_amarillas= 0
        self.tarjetas_roj= 0
        Seleccion.contador_equipos+=1
        self.codigo_equipo = Seleccion.contador_equipos
        
       
       
    def mostrar_datos(self):
        print("Jugadores")
        for i in self.jugadores:
              print (i)
        print(""")
        Total Goles: {self.goles_favor}
        Total Goles en contra: {self.goles_contra}
        Total amarillas: {self.total_tarjetas_amarillas} 
        Total Rojas: {self.tarjetas_roj}
        Fuerza equipo: {self.fuerza_equipo}
        Pais: {self.pais}
        Entrenador: {self.entrenador}
        """)
        
    def agregar_jugador(self,futbolista):
        if not isinstance(futbolista,Futbolista):
            return"el futbolista no se ha encontrado"
        for i in self.jugadores:
            if i.dorsal()==futbolista.dorsal():
                return "futbolista ya registrado"
        self.jugadores+=futbolista
    def eliminar_jugador(self,futbolista):
        if not isinstance(futbolista,Futbolista):
            return"el futbolista no se ha encontrado"
        aux=[]
        for i in self.jugadores:
            if i.dorsal()!=futbolista.dorsal():
                aux+=futbolista
        self.jugadores=aux
        aux=[]
        return self.jugadores
    def asignar_entrenador(self, entrenador):
        if not isinstance(entrenador,Entrenador):
            return "Entrenador no encontrado."
        self.entrenador=entrenador
    def calcular_fuerza_equipo(self):
        try:
            fuerza_equipo=Validaciones().fuerza_equipo_def(Validaciones().onceGrandes(self.jugadores),self.entrenador,self.pais)
        except: 
            return ("algo ha fallado, verifique sus datos, el minimo de jugadores es 11 y maximo23.")
    def registrar_resultado(self,goles_favor, goles_contra, tarjetas_am, tarjetas_roj):
        if not isinstance(goles_favor, int) or goles_favor < 0:
            return("El total de goles a favor debe ser un número entero mayor o igual a 0.")
        else:
            self.total_goles_favor += goles_favor
        if not isinstance(goles_contra, int) or goles_contra < 0:
            return("El total de goles en contra debe ser un número entero mayor o igual a 0.")
        else:
            self.total_goles_contra += goles_contra
        if not isinstance(tarjetas_am, int) and tarjetas_am < 0:
            return("El total de tarjetas amarillas debe ser un número entero mayor o igual a 0.")
        else:
            self.total_tarjetas_amarillas+= tarjetas_am
        if not isinstance(tarjetas_roj, int) or tarjetas_roj < 0:
            return("El total de tarjetas rojas debe ser un número entero mayor o igual a 0.")
        else:
            self.tarjetas_roj += tarjetas_roj
#Emanuel (arriba)

            
        
# -----------------------------------------------------------------------------------
#Kerry

class Partido:
    def __init__(self,id_partido,equipo1, equipo2, fase, fecha, mundial):

        if not Validaciones().debeser(id_partido, int):
            print(Validaciones().debeser(id_partido,int))
            return
        else: 
            self.id = id_partido
            
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.fecha = fecha
        self.fase = fase
        self.mundial = mundial
        self.goles_equipo1 = 0
        self.goles_equipo2 = 0
        self.ganador = ""
        
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
        
    ############################################################################
    def simular(self):
        equipo1 = None
        equipo2 = None
        for seleccion in Mundial.selecciones:
            if seleccion.pais.nombre == self.equipo1:
                equipo1 = seleccion
            if seleccion.pais.nombre == self.equipo2:
                equipo2 = seleccion
                
        if equipo1 is None or equipo2 is None:
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
    #############################################################################
    #Validacion de empates para juegos de fase de grupos
    def generar_ganadores(self):
        if self.goles_equipo1 == self.goles_equipo2:
            if self.fase != "Grupo":
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
        
    def mostrar_resultados(self):
        return f"{self.equipo1} {self.goles_equipo1} - {self.goles_equipo2} {self.equipo2}"

    
class Grupo:
    def __init__(self, nombre_grupo):
        if not Validaciones().debeser(nombre_grupo, str):
            print(Validaciones().debeser(nombre_grupo, str))
            return
        else:
            self.nombre_grupo = nombre_grupo
        self.equipos = []
        self.partidos = []


    def agregar_equipo(self, seleccion, fuerza):
        if len(self.equipos) >= 4:
            print("No se pueden agregar más equipos al grupo.")
            return
        if not Validaciones().debeser(seleccion, Seleccion):
            print(Validaciones().debeser(seleccion, Seleccion))
            return
        else:
            self.equipos += [[seleccion],[fuerza]]

    def jugar_partidos(self):
        if len(self.equipos) != 4:
            return "No se puede empezar los partidos porque el grupo esta incompleto"
        
        else:   
            for Equipo1 in range(len(self.equipos)):
                for Equipo2 in range(Equipo1 + 1, len(self.equipos)):
                    nombre1 = self.equipos[Equipo1][0]
                    fuerza1 = self.equipos[Equipo1][1]
                    nombre2 = self.equipos[Equipo2][0]
                    fuerza2 = self.equipos[Equipo2][1]
                    partido = Partido(len(self.partidos) +1, nombre1, nombre2, self.nombre_grupo, "20/06/2026")
              
                    partido.simular(fuerza1, fuerza2)
                    partido.generar_ganadores()
                    self.partidos += [partido] 

                    print (partido.mostrar_resultados())

    def calcular_tabla(self):
        tabla = []
        for equipo in self.equipos:
            nombre = equipo[0]
            tabla += [[nombre,0,0,0,0]]

        for partido in self.partidos:
            equipo1 = partido.equipo1
            equipo2 = partido.equipo2
            goles1 = partido.goles_equipo1
            goles2 = partido.goles_equipo2
            #funcion para buscar manualmente los indices en las filas de los equipos
            indices1 = 0
            indices2 = 0
            for indice in range(4):
                if tabla[indice][0] == equipo1:
                    indices1 = indice
                if tabla[indice][0] == equipo2:
                    indices2 = indice


            #Actualiza Goles a favor y goles en contra
            tabla[indices1][1] += goles1
            tabla[indices1][2] += goles2
            tabla[indices2][1] += goles2
            tabla[indices2][2] += goles1

            #Actualiza las diferencias de goles
            tabla[indices1][3] = tabla[indices1][1] - tabla[indices1][2]
            tabla[indices2][3] = tabla[indices2][1] - tabla[indices2][2]

            if partido.ganador == "Empate":
                tabla[indices1][4] += 1
                tabla[indices2][4] += 1

            elif partido.ganador == equipo1:
                tabla[indices1][4] += 3
            else:
                tabla[indices2][4] +=3

        for indice1 in range(4):
            for indice2 in range(0,4 - indice1 - 1):
                if tabla[indice2][4] < tabla[indice2 + 1][4]:
                    temporal = tabla[indice2]
                    tabla[indice2] = tabla[indice2 + 1]
                    tabla[indice2 + 1] = temporal

                elif tabla[indice2][4] == tabla[indice2 + 1][4]:
                    if tabla[indice2][3] < tabla[indice2 + 1][3]:
                        temporal = tabla[indice2]
                        tabla[indice2] = tabla[indice2 + 1]
                        tabla[indice2 + 1] = temporal
        return tabla
    
    
    def obtener_clasificados(self):
        tabla = self.calcular_tabla()
        clasificados = []
        for i in range(2):
            clasificados += [tabla[i][0]]
        return clasificados
    
    def mostrar_tabla(self):
        tabla = self.calcular_tabla()
        print(f"Tabla del Grupo {self.nombre_grupo}")
        print("Equipo | GF | GC | DG | P")
        for fila in tabla:
            print(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}")
     
class Fase:
    def __init__(self, fase,mundial):
        if not Validaciones().debeser(fase, str):
            print(Validaciones().debeser(fase, str))
            return
        else:
            if not Validaciones().fase_valida(fase):
                print(Validaciones().fase_valida(fase))
            else:
                self.fase = fase
        self.mundial = mundial
        self.partidos = []
    def agregar_partido(self, equipo1, equipo2, fuerza1, fuerza2):
        id_partido = len(self.partidos) + 1
        partido = Partido(id_partido, equipo1, equipo2, self.fase, "20/06/2026")
        self.partidos += [partido]
        
        
    def jugar_partidos(self):
        for partido in self.partidos:
            partido.simular(partido.fuerza1, partido.fuerza2)
            partido.generar_ganadores()
            print(partido.mostrar_resultados())
            
    def mostrar_juegos(self):
        for partido in self.partidos:
            print(f"Partido: {partido.equipo1} vs {partido.equipo2}")
            print(f"Goles: {partido.goles_equipo1} - {partido.goles_equipo2}")
            print(f"Ganador: {partido.ganador}")
            print(f"Fecha: {partido.fecha}")
    def obtener_clasificados(self):
        ganadores = []
        for partido in self.partidos:
            ganadores += [partido.ganador]
        return ganadores
    
class Mundial:
    def  __init__(self, nombre, año):
        if not Validaciones().debeser(nombre, str):
            print(Validaciones().debeser(nombre, str))
            return
        else:
            self.nombre = nombre
        if not Validaciones().debeser(año, int) or año < 1900 or año >= 2026:
            print(Validaciones().debeser(año, int))
            return
        else:
            self.año = año
        self.paises = []
        self.selecciones = []
        self.grupos = []
        self.fases = []
        campeon = None
    def agregar_pais(self, pais):
        if not isinstance(pais, Pais):
            print("El país ingresado no es válido.")
            return
        else:
            self.paises += [pais]
            archivo = open("paises.txt", "a", encoding="utf-8")
            archivo.write(f"{pais.codigo_fifa}, {pais.nombre}, {pais.continente}, {pais.ranking_fifa}\n")
            archivo.close()
    def registrar_seleccion(self, seleccion):
        if not isinstance(seleccion, Seleccion):
            print("La selección ingresada no es válida.")
            return
        else:
            self.selecciones += [seleccion]
            archivo = open("selecciones.txt", "a", encoding="utf-8")
            archivo.write(f"{seleccion.codigo_fifa}, {seleccion.nombre}, {seleccion.pais}\n")
            archivo.close()
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
            
            selecciones = 0  
            
            for i in range(cantidad_grupos):
            
                nombre_grupo = grupos[i]
                grupo = Grupo(nombre_grupo)
                
                for sele in range(4):
                    seleccion_actual = self.selecciones[selecciones]
                    fuerza_equipo = seleccion_actual.calcular_fuerza_equipo()
                    
                grupo.agregar_equipo(seleccion_actual, fuerza_equipo)
                selecciones += 1
            
            
            self.grupos += [grupo]
            
    def jugar_fase_grupos(self):
        for grupo in self.grupos:
            grupo.jugar_partidos()
            grupo.mostrar_tabla()
            print(f"Equipos clasificados del {grupo.nombre_grupo}: {grupo.obtener_clasificados()}")

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
            

 
  
    def jugar_fase_eliminatoria(self):
        for fase in self.fases:
            fase.jugar_partidos()
            fase.mostrar_juegos()
            clasificados = fase.obtener_clasificados()
            print(f"Equipos clasificados de la {fase.fase}: {clasificados}")
            
    def determinar_campeon(self):
        if self.fases:
            ultima_fase = self.fases[-1]
            if ultima_fase.partidos:
                ultimo_partido = ultima_fase.partidos[-1]
                self.campeon = ultimo_partido.ganador
                print(f"El campeón del Mundial {self.nombre} {self.año} es: {self.campeon}")
            else:
                print("No se han jugado partidos en la última fase.")
                return
    def mostrar_tabla_general(self):
        possicion = 1
        print(f"Table General del Mundial {self.nombre} {self.año}")
        print("Posicion | Equipo | GF| GC | DG | Puntos")
        for grupo in self.grupos:
            tabla = grupo.calcular_tabla()
            for fila in tabla:
                print(f"{possicion} | {fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}")
                possicion += 1
    
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
            
                
        
        

        














