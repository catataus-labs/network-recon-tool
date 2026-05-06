import socket
def check_port(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1.0)
    result = client.connect_ex((ip, port))
    if result == 0:
        print(f"[*] Port {port} is OPEN on {ip}")
    else:
        print(f"[!] Port {port} is CLOSED/FILTERED on {ip}")
    client.close()
target_ip = "8.8.8.8"
target_port = 80

check_port(target_ip, target_port)
