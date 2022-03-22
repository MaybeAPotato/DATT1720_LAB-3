import http.server
import socketserver

PORT = 3030 #8080, 8887, 8898

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT), handler) as httpd:
    print("PORT: ", PORT)
    httpd.serve_forever()#Keep it running forever