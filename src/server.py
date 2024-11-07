import logging
from http.server import BaseHTTPRequestHandler


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("pages/contacts.html", "r", encoding="utf-8") as page:
            page_content = page.read()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode("utf-8")
        logging.debug(data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("Ok!", "utf-8"))
