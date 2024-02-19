import json
import os

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @staticmethod
    def guardar_clientes(clientes):
        with open('clientes.json', 'w') as file:
            json.dump(clientes, file, indent=4)

    @staticmethod
    def cargar_clientes():
        if not os.path.exists('clientes.json'):
            return []
        with open('clientes.json', 'r') as file:
            return json.load(file)

    def crear_cliente(self):
        clientes = Customer.cargar_clientes()
        clientes.append({
            'name': self.name,
            'email': self.email
        })
        Customer.guardar_clientes(clientes)

    def eliminar_cliente(self):
        clientes = Customer.cargar_clientes()
        clientes = [cliente for cliente in clientes if cliente['name'] != self.name]
        Customer.guardar_clientes(clientes)

    def mostrar_info_cliente(self):
        clientes = Customer.cargar_clientes()
        cliente = next((c for c in clientes if c['name'] == self.name), None)
        if cliente:
            print(json.dumps(cliente, indent=4))
        else:
            print("Cliente no encontrado.")

    def modificar_info_cliente(self, new_email=None):
        clientes = Customer.cargar_clientes()
        for cliente in clientes:
            if cliente['name'] == self.name:
                cliente['email'] = new_email if new_email is not None else cliente['email']
        Customer.guardar_clientes(clientes)