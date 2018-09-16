import sys
import board
from settings import NetworkSettings
from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser, os


class BattleshipServer(BaseHTTPRequestHandler):

    #this needs to display the boards
    def do_GET(self):

        html_name = str(self.path).replace("/", "")
        txt_name = html_name.replace(".html", ".txt")
        text = open(txt_name, 'r')

        print(txt_name)
        print(html_name)
        with open(html_name, "w") as out:
            out.write("<!DOCTYPE html>\n")
            out.write("<html>\n<head>\n<style>\n")

            out.write("line-height: 0.7 </style>\n</head>\n<body>\n")
            out.write("<p>\n")

            for line in text.readlines():
                out.write(line + "<br>\n")
            out.write("</p>\n</body>\n</html>")

        f = open(html_name, 'rb')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f.read())


    #POST
    def do_POST(self):

        length = int(self.headers["Content-Length"])
        print("Data: " + str(self.rfile.read(length), "utf-8"))

        response = bytes("Response", "utf-8")

        self.send_response(200)
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()

        self.wfile.write(response)


def make_connection(port, network_settings, use_local, name):
    if use_local == 0:
        ip = network_settings.IP
        print("using %s as IP address" % network_settings.IP)
    elif use_local == 1:
        ip = network_settings.LOCAL_IP
        print("using %s as IP address" % network_settings.LOCAL_IP)
    else:
        print("Wrong IP choice value")
        return False

    server = HTTPServer((ip, port), BattleshipServer)
    server.serve_forever()


if __name__ == '__main__':
    network_settings = NetworkSettings()
    port = int(sys.argv[1])
    file_name = sys.argv[2]
    #0 for Brodcast IP, 1 for local ip
    use_local = int(sys.argv[3])

    make_connection(port, network_settings, use_local, file_name)
