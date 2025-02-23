# Simulaci-n-de-un-Sistema-de-Atenci-n-en-un-Banco
simulacion de un sistema de atencion de un banco con colas

Descripción del programa:

1️Importación de la librería deque
Se usa deque de collections porque es más eficiente que una lista para manejar colas. Permite agregar y quitar elementos de ambos extremos en tiempo constante 
O(1).

2️ Clase Banco
Constructor __init__:

Se crean dos colas:
cola_prioritaria: Para clientes con prioridad.
cola_general: Para clientes normales.
Método agregar_cliente(nombre, prioritario):

Si prioritario es True, se agrega el cliente a cola_prioritaria.
Si es False, se agrega a cola_general.
Método atender_cliente():

Atiende primero a clientes de cola_prioritaria, si hay alguno.
Si no hay clientes prioritarios, atiende a los de cola_general.
Si no hay clientes en ninguna cola, muestra un mensaje de advertencia.
Método mostrar_espera():

Muestra la cantidad total de clientes en espera.
Muestra las listas de clientes en cada cola (prioritaria y general).

3️ Función menu()
Crea una instancia de Banco para manejar las operaciones.

Muestra un menú interactivo con 4 opciones:

Agregar cliente: Pide el nombre y pregunta si es prioritario.
Atender cliente: Atiende al siguiente cliente según prioridad.
Mostrar clientes en espera: Muestra la cantidad y listas de clientes.
Salir: Termina el programa.
Utiliza un while True para mantener el menú en ejecución hasta que el usuario seleccione la opción "Salir".

Ejemplo de Uso en Consola:
--- Menú del Banco ---
1. Agregar cliente
2. Atender cliente
3. Mostrar cola de espera
4. Salir
Seleccione una opción: 1
Ingrese el nombre del cliente: Juan Pérez
¿Es cliente prioritario? (s/n): n
 Cliente Juan Pérez agregado a la cola.

Seleccione una opción: 1
Ingrese el nombre del cliente: María López
¿Es cliente prioritario? (s/n): s
 Cliente PRIORITARIO María López agregado a la cola.

Seleccione una opción: 3
 Clientes en espera: 2
 Prioritarios: ['María López']
 Generales: ['Juan Pérez']

Seleccione una opción: 2
 Atendiendo a cliente PRIORITARIO: María López
