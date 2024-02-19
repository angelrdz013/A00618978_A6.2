import json
import os

class Reservation:
    def __init__(self, customer_name, hotel_name, room_number, start_date, end_date):
        self.customer_name = customer_name
        self.hotel_name = hotel_name
        self.room_number = room_number
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def guardar_reservas(reservas):
        with open('reservas.json', 'w') as file:
            json.dump(reservas, file, indent=4)
    
    @staticmethod
    def cargar_reservas():
        if not os.path.exists('reservas.json'):
            return []
        with open('reservas.json', 'r') as file:
            return json.load(file)

    def crear_reserva(self):
        reservas = Reservation.cargar_reservas()
        reservas.append({
            'customer_name': self.customer_name,
            'hotel_name': self.hotel_name,
            'room_number': self.room_number,
            'start_date': self.start_date,
            'end_date': self.end_date
        })
        Reservation.guardar_reservas(reservas)

    def cancelar_reserva(self, reserva_id):
        reservas = Reservation.cargar_reservas()
        reservas = [reserva for reserva in reservas if reserva.get('id', '') != reserva_id]
        Reservation.guardar_reservas(reservas)