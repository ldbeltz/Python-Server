import socket
HOST = ''    # Colocar IP do servidor
PORT = 5000  # Colocar porta compartilhada
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print 'Para sair use CTRL+X\n'
msg = raw_input()
while msg != '\x18':
    udp.sendto (msg, dest)
    msg = raw_input()
udp.close()