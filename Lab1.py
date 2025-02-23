from collections import deque  # Importamos deque para manejar la cola de clientes

class Banco:
    def __init__(self):
        """
        Constructor de la clase Banco.
        Se crean dos colas:
        - cola_prioritaria: Para clientes con prioridad (ej. personas mayores, con discapacidad).
        - cola_general: Para clientes normales.
        """
        self.cola_general = deque()  # Cola para clientes normales
        self.cola_prioritaria = deque()  # Cola para clientes prioritarios

    def agregar_cliente(self, nombre, prioritario=False):
        """
        Agrega un cliente a la cola correspondiente.
        Parámetros:
        - nombre: Nombre del cliente.
        - prioritario: Booleano que indica si el cliente tiene prioridad.
        """
        if prioritario:
            self.cola_prioritaria.append(nombre)  # Agrega a la cola prioritaria
            print(f" Cliente PRIORITARIO {nombre} agregado a la cola.")
        else:
            self.cola_general.append(nombre)  # Agrega a la cola normal
            print(f" Cliente {nombre} agregado a la cola.")