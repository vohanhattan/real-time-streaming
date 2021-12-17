import socket
import time

import requests, json

"""
Stock price stream example for this program
"""

def main():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432 # can change this if you want

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = (HOST, PORT)

    sock.connect(server_address)
    api_key = "97af345a6888df416133f36767d2fe89"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    while True:
        response = requests.get(complete_url)
        x = response.json()
        y = x["main"]
        # get live temperature of can tho
        temperature = y["temp"]-273.15
        # get live pressure
        pressure = y["pressure"]
	# get live humidity
        humidity = y["humidity"]
        print("temperature: " ,temperature,"pressure: ", pressure,"humidity: ",humidity)

        send_str = '{"id":1337, "value": ['+str(temperature)+', '+ str(pressure)+','+str(humidity)+'], "type":"line","active_points": 20, "label":"value", "legend": ["temperature (C)", "pressure (hPa)","humidity (%)"], "name":"Weather forecast Example",  "borderColor":["#3e95cd", "#e8c3b9"], "backgroundColor" :["#3e95cd","#e8c3b9"]}'
        sock.sendall(str.encode(send_str))

        time.sleep(3600)

if __name__ == '__main__':
    main()

