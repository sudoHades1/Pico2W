import wifi
import socketpool
import time

# Wi-Fi credentials
SSID = "wifiname"
PASSWORD = "password"

print("Connecting to WiFi...")

wifi.radio.connect(SSID, PASSWORD)

print("Connected!")
print("IP address:", wifi.radio.ipv4_address)

# Create socket pool
pool = socketpool.SocketPool(wifi.radio)

# Create server socket
server = pool.socket(pool.AF_INET, pool.SOCK_STREAM)
server.bind(("0.0.0.0", 8082))
server.listen(1)

print("Web server running...")

while True:
    conn, addr = server.accept()
    print("Client connected from", addr)

     # For circuitpython
    buffer = bytearray(1024)
    size = conn.recv_into(buffer)

    request = buffer[:size]
    print(request)

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n\r\n"
        "<html><body><h1>Pico OK</h1></body></html>"
    )

    print("Sending response...")
    conn.send(response)
    conn.close()
