import socket  # Importa socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea Socket TCP
host = socket.gethostname()  # Toma el nombre de la maquina local
port = 12345  # Reserva el puerto
s.bind((host, port))  # Vincula el host al puerto
f = open('../ARCHIVOS/archivo_100M', 'r')
s.listen(5)  # Espera por la conexion del cliente.
l = f.read(1024)
while True:
    buffer = ''
    c, addr = s.accept()  # Establece la conexion con el cliente
    print('Conexion recivida de: ', addr)
    # Lee el tipo de archivo que necesita el cliente:
    data = c.recv(1024)
    if data:
        buffer += data
        print(buffer)
    else:
        break;
    while l:
        print("Enviando...")
        s.send(l)
        l = f.read(1024)
    f.close()
    print("Enviado exitosamente")
    s.shutdown(socket.SHUT_WR)
    c.send('Gracias por conectarse. Archivo enviado.')
    c.close()  # Cerrar conexion
