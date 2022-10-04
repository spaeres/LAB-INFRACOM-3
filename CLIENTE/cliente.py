import socket
import sys
import os
import errno

#Hacer el archivo hash

#Escribir el log(?)
def escribir_directorio():
    try:
        os.mkdir('Archivos recibidos')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server
# given by the caller
host = socket.gethostname
port = 12345
#server_address = (host, port)
server_address = (sys.argv[1], 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    #el buffer y todo lo demas
    #necesito archivos?
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(1024)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    sock.close()