import socket

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def scan_ports(ip, start_port, end_port):
    print(f"\n🔍 Scanning IP: {ip} from port {start_port} to {end_port}\n")
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
    
    if open_ports:
        print("✅ Open ports found:")
        for port in open_ports:
            print(f" - Port {port}")
    else:
        print("❌ No open ports found in the given range.")

# --- User Input Section ---
ip = input("Enter IP address to scan (e.g., 127.0.0.1): ")

if not is_valid_ip(ip):
    print("❗ Invalid IP address.")
else:
    try:
        start_port = int(input("Enter starting port number: "))
        end_port = int(input("Enter ending port number: "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("❗ Invalid port range. Ports must be between 0 and 65535.")
        else:
            scan_ports(ip, start_port, end_port)
    except ValueError:
        print("❗ Please enter valid numbers for ports.")
