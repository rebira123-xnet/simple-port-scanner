import socket

print("Simple Port Scanner")

target = input("Enter website or IP: ")

# convert website to IP
ip = socket.gethostbyname(target)

# common ports
ports = [21, 22, 23, 25, 53, 80, 443]

for port in ports:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(1)

    result = s.connect_ex((ip, port))

    if result == 0:
        print("Port", port, "is open")

    s.close()

print("Scan finished")
