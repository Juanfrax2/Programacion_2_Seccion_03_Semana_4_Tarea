class Avión:
    def __init__(self, nro_avión, modelo, asientos):
        self.nro_avión = nro_avión
        self.modelo = modelo
        self.asientos = asientos

    def __str__(self):
        return f"ID avión: {self.nro_avión}. Avión: {self.modelo}. Asientos avión: {self.asientos}"

class Vuelo:
    
    def __init__(self, nro_vuelo, origen, destino, fecha, hora, avión_asignado):
        self.nro_vuelo = nro_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.avión_asignado = avión_asignado
        self.reservaciones = []

    def agregar_reservación(self, pasajero):
        self.reservaciones.append(pasajero)


    def ver_pasajeros_vuelo(self):
        for i in self.reservaciones:
            print(i)


    def __str__(self):
        return f"ID vuelo: {self.nro_vuelo}. Avión asignado: {self.avión_asignado}. Va desde {self.origen} hasta {self.destino}. Despega el {self.fecha} a las {self.hora} horas"


class Pasajero:
    def __init__(self, nro_pasajero, nombre, número_pasaporte):
        self.nro_pasajero = nro_pasajero
        self.nombre = nombre
        self.número_pasaporte = número_pasaporte
        self.vuelos_reservados = []
    
    def agregar_reservación(self, vuelo):
        self.vuelos_reservados.append(vuelo)
    
    def mostrar_vuelos(self):
        for i in self.vuelos_reservados:
            print(i)
    
    def __str__(self):
        return f"Id pasajero: {self.nro_pasajero}. Nombre pasajero: {self.nombre}. Número del pasaporte: {self.número_pasaporte}"
    
class Reservación:
    def __init__(self, nro_reservación, pasajero, vuelo):
        self.nro_reservación = nro_reservación
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = "Reservado"
        pasajero.agregar_reservación(vuelo)
        vuelo.agregar_reservación(pasajero)

    def estado_reserva(self, reservación):
        self.estado = "Cancelado"
        print(f"La reservación con el ID {reservación.nro_reservación} de {reservación.pasajero.nombre} ha sido {self.estado}")

    def __str__(self):
        return f"ID reservación: {self.nro_reservación}. {self.pasajero}. {self.vuelo}. Estado: {self.estado}"
    

class Aerolinea:
    def __init__(self):
        self.aviones = ["Aviones:"]
        self.vuelos = ["Vuelos:"]
        self.pasajeros = ["Pasajeros:"]
        self.reservaciones = []
        self.nro_avión = 1
        self.nro_vuelo = 1
        self.nro_pasajero = 1
        self.numero_reservacion_actual = 1

    def crear_avion(self):
        modelo = str(input("Ingrese el modelo del avión: "))
        asientos = int(input("Ingrese el número de asientos que tiene el avión: "))
        avión = Avión(self.nro_vuelo, modelo, asientos)
        self.nro_avión += 1
        self.aviones.append(avión)
    
    def mostrar_aviones(self):
        if len(self.aviones) == 1:
            print("Aún no hay aviones disponibles")
        for avión in self.aviones:
            print(avión)

    def crear_vuelo(self):
        if len(self.aviones) == 1:
            print("No hay aviones disponibles para llevar a cabo el vuelo.")
            return
        origen = str(input("Lugar de despegue del vuelo: "))
        destino = str(input("Lugar de destino del vuelo: "))
        fecha = str(input("Fecha de despegue: "))
        hora = str(input("Hora de despegue: "))
        for i in self.aviones:
            print(i)
        avión_asignado = self.aviones[int(input("\nDigite la ID del avión que desea elegir para el vuelo: "))]
        vuelo = Vuelo(self.nro_vuelo, origen, destino, fecha, hora, avión_asignado)
        self.nro_vuelo += 1
        self.vuelos.append(vuelo)
        return

    def mostrar_vuelos(self):
        if len(self.vuelos) == 1:
            print("Aún no hay vuelos disponibles")
        for vuelos in self.vuelos:
            print(vuelos)

    def crear_pasajero(self):
        nombre = str(input("Ingrese el nombre del pasajero: "))
        número_pasaporte = int(input("Digite el número de pasaporte del pasajero: "))
        pasajero = Pasajero(self.nro_pasajero, nombre, número_pasaporte)
        self.nro_pasajero += 1
        self.pasajeros.append(pasajero)
        
    def mostrar_pasajeros(self):
        if len(self.pasajeros) == 1:
            print("Aún no hay pasajeros inscritos")
        for pasajero in self.pasajeros:
            print(pasajero)
        
    def crear_reservación(self):
        if len(self.pasajeros) == 1:
            print("No hay pasajeros inscritos en la aerolinea")
            return
        if len(self.vuelos) == 1:
            print("No hay vuelos disponibles")   
            return
        
        for i in self.pasajeros:
            print(i)

        pasajero = self.pasajeros[int(input("Seleccione al pasajero al que desea hacer la reservacion con su ID: "))]
        
        for i in self.vuelos:
            print(i)

        vuelo = self.vuelos[int(input("Seleccione el vuelo que se le asignara a la reservacion con su ID:"))]

        for i in self.reservaciones:
            if i.pasajero == pasajero and i.vuelo == vuelo:
                print("La reservación ya existe.")
                return   
        if vuelo.avión_asignado.asientos <= len(vuelo.reservaciones):
            print("No hay asientos desocupados en el avion para realizar la reservacion.")
            return
        reserva = Reservación(self.numero_reservacion_actual, pasajero, vuelo)
        self.numero_reservacion_actual += 1
        self.reservaciones.append(reserva)


    def mostrar_reservaciones(self):
        if len(self.reservaciones) == 0:
            print("Aún no hay reservaciones de ningún pasajero en la aerolinea")
        for reservas in self.reservaciones:
            print(reservas)

    def mostrar_reservaciones_pasajero(self):
        if len(self.pasajeros) == 1:
            print("Aún no hay pasajeros inscritos")
            return
        for i in self.pasajeros:
            print(i)
        pasajero = self.pasajeros[int(input("Seleccione al pasajero(Coloque el numero de la posicion en la lista del pasajero del que desea ver sus vuelos reservados (la lista comienza desde 0): "))]
        return pasajero.mostrar_vuelos()

    def mostrar_pasajeros_vuelo(self):
        if len(self.vuelos) == 1:
            print("No hay vuelos para mostrar sus pasajeros.")
            return
        for vuelo in self.vuelos:
            print(vuelo)        
        vuelo = self.vuelos[int(input("Seleccione el vuelo(Coloque el numero de la posicion en la lista del vuelo del que desea ver sus pasajeros (la lista comienza desde 0): "))]
        return vuelo.ver_pasajeros_vuelo()
    
    def cancelar_reservación(self):
        if len(self.reservaciones) == 0:
            print("Aún no hay reservaciones en la aerolinea")
            return
        for i in self.reservaciones:
            print(i)
        reservación = self.reservaciones[int(input("Seleccione la reservacion(al ID de la reservación restele 1 y digite el resultado para seleccionar la reservación): "))]
        return reservación.estado_reserva(reservación)


al = Aerolinea()

def funcionalidades():
    clave = int(input("\nSi desea agregar un avión presione 1.\nSi desea agregar un vuelo presione 2.\nSi desea agregar un pasajero presione 3.\nSi desea reservar un vuelo a un pasajero presione 4.\nSi desea ver los aviones disponibles presione 5.\nSi desea ver los vuelos disponibles presione 6.\nSi desea ver los pasajeros inscritos en la aerolinea presione 7.\nSi desea ver todas las reservaciones de la aerolinea presione 8.\nSi desea ver las reservas de algún pasajero presione 9.\nSi desea ver los pasajeros de un vuelo en especifico digite 10.\nSi desea cancelar una reservacion digite 11.\nSi desea salir del programa digite 12.\nIngrese numero: "))
    if clave == 1:
        al.crear_avion()
        "\n"
    if clave == 2:
        al.crear_vuelo()
        "\n"
    if clave == 3:
        al.crear_pasajero()
        "\n"
    if clave == 4:
        al.crear_reservación()
        "\n"
    if clave == 5:
        al.mostrar_aviones()
        "\n"
    if clave == 6:
        al.mostrar_vuelos()
        "\n"
    if clave == 7:
        al.mostrar_pasajeros()
        "\n"
    if clave == 8:
        al.mostrar_reservaciones()
        "\n"
    if clave == 9:
        al.mostrar_reservaciones_pasajero()
    if clave == 10:
        al.mostrar_pasajeros_vuelo()
        "\n"
    if clave == 11:
        al.cancelar_reservación()
        "\n"
    if clave == 12:
        return   
    
    input("Presione ENTER")
    return funcionalidades()
    
print("\n¡Bienvenido(a) aerolineas TOPGUN!, ¿qué desea hacer?:")

funcionalidades()




