import http.server
import socketserver

PORT = 80
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("Serving at port %s" % PORT)
httpd.serve_forever()
