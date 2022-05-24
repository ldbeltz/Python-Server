from curses.ascii import isupper
import  socket
HOST = ''              # Colocar IP do servidor
PORT = 5000            # Colocar porta compartilhada
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
while True:
    msg, cliente = udp.recvfrom(1024)
    if (msg.isupper()):
        msg = msg.lower()
    else:
        msg = msg.upper
    print cliente, msg
udp.close()