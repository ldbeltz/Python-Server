from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import time

hostIP = ""
porta = 5000

class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        now = datetime.now()
        hora_atual = now.strftime("%H:%M:%S")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Servidor HTTP</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Agora sao: %s</p>" % (hora_atual), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    servidorWeb = HTTPServer((hostIP, porta), Servidor)
    print("Servidor iniciado em %s:%s" % (hostIP, porta))

    try:
        servidorWeb.serve_forever()
    except KeyboardInterrupt:
        pass

    servidorWeb.server_close()
    print("Servidor interrompido.")