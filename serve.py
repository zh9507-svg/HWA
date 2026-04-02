import http.server
import socketserver
import os

PORT = 8080
os.chdir("/Users/zaidkhokhar/Documents/Claude/HWA")

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
