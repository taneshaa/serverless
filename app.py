from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)
        print(dic)
        url = 'https://restcountries.com/v3.1/name/'
        if 'name' in dic:
            r = requests.get(url + dic['name'])
            capital = ""
            info = r.json()
            for cap in info:
                country_capital = cap['capital'][0]
                capital += country_capital
            message = f"The capital of {dic['name']} is {capital}"
        else:
            message = 'Please give us a country'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
