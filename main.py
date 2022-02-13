import time

from PicImageSearch import Ascii2D
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib import parse

host = ('0.0.0.0', 8080)


class Request(BaseHTTPRequestHandler):

    def do_GET(self):
        res = None
        if self.path.find("color") != -1:
            path = parse.unquote(self.path)[7:]
            ascii2d = Ascii2D(bovw=False)
        elif self.path.find("bovw") != -1:
            path = parse.unquote(self.path)[6:]
            ascii2d = Ascii2D(bovw=True)
        else:
            self.send_error(403)
            return
        time.sleep(6)
        res = ascii2d.search(path)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(str(res.origin).encode('utf-8'))


if __name__ == '__main__':
    server = ThreadingHTTPServer(host, Request)
    server.serve_forever()
