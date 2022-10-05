import socket
import os
import errno

#Hacer el archivo hash
nombre = ""
def nombrar_cliente(n_cliente):
    nombre = "cliente"+n_cliente
#Escribir el log(?)
def escribir_directorio():
    try:
        os.mkdir('ArchivosRecibidos')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server
# given by the caller
host = '192.168.20.34'
port = 29170
hash = ""
server_address = (host, port)
#server_address = (sys.argv[1], 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
escribir_directorio()

try:
    message = b'Hola, estoy listo para recibir archivos |'
    sock.send(message)

    dataInicial = sock.recv(1024)
    print('Recibi tu mensaje: {!r}'.format(dataInicial))

    entrada1 = input('Que archivo quieres? 100 MB o 250 MB? (Por favor escribir unicamente el que desea: Ej: "100MB")')
    rutaDeseada = ''
    if(entrada1=="100MB"):
        rutaDeseada = b'archivo_100M'
    elif(entrada1=="250MB"):
        rutaDeseada = b'archivo_250M'

    sock.send(rutaDeseada)

    while True:
        data = sock.recv(10024)
        print('El mensaje fue recibido {!r}'.format(data))

finally:
    sock.close()