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
host = '192.168.85.128'
port = 12345
server_address = (host, port)
#server_address = (sys.argv[1], 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
escribir_directorio()

try:
    #el buffer y todo lo demas
    #necesito archivos?
    
    #message = b'This is the message.  It will be repeated.'
    #print('sending {!r}'.format(message))
    #sock.recv(message)
    
    #data1 = sock.recv(1024)

    #amount_received = 0
    #amount_expected = len(message)
    #while amount_received < amount_expected:
    while True:
        data = sock.recv(1024)
        print('El mensaje fue recibido {!r}'.format(data))

finally:
    sock.close()