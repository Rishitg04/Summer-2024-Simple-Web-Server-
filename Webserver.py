from http.server import HTTPServer, BaseHTTPRequestHandler    #To create server and handle requests
from urllib.parse import parse_qs                             #To parse query strings from URLs

HOST = "192.168.1.33"
PORT = 9999

class MyTest(BaseHTTPRequestHandler):
    #Handles GET requests
    def do_GET(self):
        self.send_response(200)                               #Sends an OK signal telling the client request was performed successfully
        self.send_header("Content-type", "text/html")         #Indicates body of response will be html
        self.end_headers()

        html = """
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Stock Price Checker</title>
  </head>
  <body>
    <h1>Stock Price Checker</h1>
    <p>
      Enter a ticker symbol and a time interval to get a graph of the price!
    </p>
    <form method="POST" action="info">
    <!-- Tells it where to go. If not there it will be loaded on the same page -->
      <div>
        <label for="symbol">Ticker Symbol</label>
        <input type="text" name="symbol" placeholder="Enter ticker symbol" />
      </div>
      <div>
        <input
          type="radio"
          id="daily"
          name="interval"
          value="TIME_SERIES_DAILY"
          checked
        />
        <label for="daily">Daily</label>
      </div>
 
      <div>
        <input type="radio" 
	  id="weekly" 
          name="interval" 
          value="TIME_SERIES_WEEKLY" />
        <label for="weekly">Weekly</label>
      </div>
 
      <div>
        <input
          type="radio"
          id="monthly"
          name="interval"
          value="TIME_SERIES_MONTHLY"
        />
        <label for="monthly">Monthly</label>
      </div> 
      <button type="submit">Submit</button>
    </form>	
  </body>
</html>
"""
        self.wfile.write(bytes(html,"utf-8"))                   #Converts our html string to bytes and writes it out   

    #Handles POST requests
    def do_POST(self):
        #Gets the data which was entered into our form
        content_length = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_length).decode('utf-8')
        fields = parse_qs(post_data)
        data = ""

        #Print the received form data to the console
        print("Form data received:")
        for key, value in fields.items():
            data += f"{key}: {value[0]}" +f"\n"
            print(f"{key}: {value[0]}")


        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = f"<html><body><h1>Form submitted successfully</h1><p>{data}</p></body></html>"
        self.wfile.write(response.encode('utf-8'))

server = HTTPServer((HOST,PORT), MyTest)                        
print("Server now running")
server.serve_forever()

