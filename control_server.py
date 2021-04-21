from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import sys, os
import urllib
import itertools

hostName = sys.argv[1]
serverPort = 28080

class CommandServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        if self.path.split("/")[1] == "getData":
            self.send_header("Content-type","application/json")
            self.end_headers()
            index = self.path.split("/")[2]
            with open('data/' + os.listdir('data')[int(index)]) as f:
                print("Returning", os.listdir('data')[int(index)])
                if len(self.path.split("/")) > 3:
                    orderIndex = self.path.split("/")[3]
                    k = self.path.split("/")[4]
                    obj = json.load(f)
                    list(itertools.permutation(list(range(obj['transactions'].count('transaction'))])), k))[orderIndex]
                else:
                    self.wfile.write(bytes(json.dumps(json.load(f)), "utf-8"))

        else:
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Command Control Server Landing Page</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is a placeholder.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = urllib.parse.unquote_plus(str(post_data))
        output = data.split('=')[1]
        index = int(self.path.split("/")[2])
        bundleName = os.listdir('data')[int(index)].split('.')[0]
        with open("output/" + bundleName + ".txt", "w") as f:
            f.write(output)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps({"response": "success"}), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), CommandServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
