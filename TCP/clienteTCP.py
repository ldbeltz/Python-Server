import socket
HOST = ''     # Colocar IP do servidor
PORT = 5000   # Colocar porta compartilhada
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X\n'
msg = raw_input()
while msg != '\x18':
    tcp.send (msg)
    msg = raw_input()
tcp.close()