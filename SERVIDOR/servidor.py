import socket  # Importa socket
import hashlib
import constantes as cons


def hash_archivo(nombre_archivo):
    md5_hash = hashlib.md5()
    if nombre_archivo == cons.NOMBRE_ARCHIVO_100M:
        a_file = open(cons.RUTA_ARCHIVO_100M, "rb")
    else:
        a_file = open(cons.RUTA_ARCHIVO_250M, "rb")
    content = a_file.read()
    md5_hash.update(content)

    digest = md5_hash.hexdigest()
    return digest


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea Socket TCP
host = socket.gethostname()  # Toma el nombre de la maquina local
port = 12345  # Reserva el puerto
s.bind((host, port))  # Vincula el host al puerto

s.listen(5)  # Espera por la conexion del cliente.

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
        break
    f = ''
    nombre_archivo = ''
    if buffer == cons.NOMBRE_ARCHIVO_100M:
        nombre_archivo = cons.NOMBRE_ARCHIVO_100M
        f = open(cons.RUTA_ARCHIVO_100M, 'r')
    else:
        nombre_archivo = cons.NOMBRE_ARCHIVO_250M
        f = open(cons.RUTA_ARCHIVO_250M, 'r')
    hash = hash_archivo(nombre_archivo)
    l = f.read(1024)
    print("Enviando Hash...")
    s.send(hash)
    while l:
        print("Enviando Archivo...")
        s.send(l)
        l = f.read(1024)
    f.close()
    print("Enviado exitosamente")
    s.shutdown(socket.SHUT_WR)
    c.send('Gracias por conectarse. Archivo enviado.')
    c.close()  # Cerrar conexion
