import json
import os

class Hotel:
    def __init__(self, name, location, rooms):
        self.name = name
        self.location = location
        self.rooms = rooms  
        self.reservations = []  

    def guardar_hoteles(hoteles):
        with open('hoteles.json', 'w') as file:
            json.dump(hoteles, file, indent=4)

    def cargar_hoteles():
        if not os.path.exists('hoteles.json'):
            return []
        with open('hoteles.json', 'r') as file:
            return json.load(file)

    def crear_hotel(self):
        hoteles = Hotel.cargar_hoteles()
        hoteles.append({
            'name': self.name,
            'location': self.location,
            'rooms': self.rooms,
            'reservations': self.reservations
        })
        Hotel.guardar_hoteles(hoteles)

    def eliminar_hotel(self):
        hoteles = Hotel.cargar_hoteles()
        hoteles = [hotel for hotel in hoteles if hotel['name'] != self.name]
        Hotel.guardar_hoteles(hoteles)

    def mostrar_info_hotel(self):
        hoteles = Hotel.cargar_hoteles()
        hotel = next((h for h in hoteles if h['name'] == self.name), None)
        if hotel:
            print(json.dumps(hotel, indent=4))
        else:
            print("Hotel no encontrado.")

    def modificar_info_hotel(self, new_location=None, new_rooms=None):
        hoteles = Hotel.cargar_hoteles()
        for hotel in hoteles:
            if hotel['name'] == self.name:
                hotel['location'] = new_location if new_location is not None else hotel['location']
                hotel['rooms'] = new_rooms if new_rooms is not None else hotel['rooms']
        Hotel.guardar_hoteles(hoteles)

    def reservar_habitacion(self, room_number, customer_name, start_date, end_date):
        self.reservations.append({
            'room_number': room_number, 
            'customer_name': customer_name, 
            'start_date': start_date, 
            'end_date': end_date
        })
        self.modificar_hotel()  

    def cancelar_reservacion(self, reservation_id):
        self.reservations = [r for r in self.reservations if r['id'] != reservation_id]
        self.modificar_hotel()  