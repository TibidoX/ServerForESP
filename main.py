import http.server
import socketserver

port = 8080


def func():
    print('Called')


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/hello'):
            self.send_response(200)
            func()
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Hello, world!')
        if self.path.endswith('/'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            s = '''
            <!DOCTYPE html>
            <html>
            <head>
              <title>Enter your message</title>
            </head>
            <body>
              <form>
                  <input type="text" name="userText" placeholder="here">
                  <button type="submit">Send</button>
              </form>
            </body>
            </html>
            '''
            str = '''
            <!DOCTYPE html>
            <html>
            <body>
             <form action="http://193.164.149.123:8080" method="POST">
                <input type="text" name="text">
                <input type="submit" value="Send">
             </form>
            </body>
            </html>
            '''
            self.wfile.write(str.encode())
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f'Received data: {post_data.decode()}')
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

httpd = socketserver.TCPServer(("", 8080), Handler)
httpd.serve_forever()
