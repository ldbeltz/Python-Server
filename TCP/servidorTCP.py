import socket
HOST = ''              # Colocar IP do servidor
PORT = 5000            # Colocar porta compartilhada
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        if (msg.isupper()):
            msg = msg.lower()
        else:
            msg = msg.upper
        print cliente, msg
    print 'Finalizando conexao do cliente', cliente
    con.close()