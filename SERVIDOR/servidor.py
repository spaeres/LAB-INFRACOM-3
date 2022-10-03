import socket  # Importa socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea Socket TCP
host = socket.gethostname()  # Toma el nombre de la maquina local
port = 12345  # Reserva el puerto
s.bind((host, port))  # Vincula el host al puerto
f = open('torecv.png', 'wb')
s.listen(5)  # Espera por la conexion del cliente.
while True:
    c, addr = s.accept()  # Establece la conexion con el cliente
    print('Got connection from', addr)
    print("Receiving...")
    l = c.recv(1024)
    while l:
        print("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print("Done Receiving")
    c.send('Thank you for connecting')
    c.close()  # Close the connection
