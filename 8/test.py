from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class ServerWorking(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes("Custom server is working", "utf-8"))

server_address=('', 8080)
server = HTTPServer(server_address, ServerWorking)
server.serve_forever()