import socket
import sys
from datetime import datetime

#list common ports as constant
COMMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"
}

#scan port function
def scan_port(target, port, timeout=1):
    try:
        #create socket object
        #using IPv4
        #using TCP -> makes a full connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        #attempt to connect
        result = sock.connect_ex((target, port)) #ex returns an error message

        #get service name if available
        service = COMMMON_PORTS.get(port, "Unknown")

        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSED"
        
        sock.close()
        return port, status, service

    except socket.gaierror: #python fails to resolve hostname
        return port, "ERROR", "Hostname resolution failed."
    except socket.error: #connection error
        return port, "ERROR", "Connection error"

#create function that adds user interface element
def scan_single_port(target, port):
    print(f"\n[*] Scanning{target} on port {port}...")
    print(f"[*] Scan started at {datetime.now().strftime('%y-%m-%d %H:%M:%S')}") #exactly when scan started for documentation

    port_num, status, service = scan_port(target, port)

    if status == "OPEN":
        print(f"[+] Port {port_num}/{service}: {status}")
    elif status == "CLOSED":
        print(f"[-] Port {port_num}/{service}: {status}")
    else:
        print(f"[!] Port {port_num}: {status} - {service}")

#create function that scans multiple ports

def scan_multiple_ports(target, ports):
    print(f"\n[*] Scanning {target} on {len(ports)} ports...")
    print(f"\n[*] Scan started at {datetime.now().strftime('%y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    open_ports = [] #establish list
    closed_ports = []

    for port in ports:
        port_num, status, service = scan_port(target, port)

        if status == "OPEN":
            print(f"\n[+] Port {port_num}/{service}: {status}")
            open_ports.append((port_num, service)) #add to list
        elif status == "CLOSED":
            print(f"\n[-] Port {port_num}/{service}: {status}")
            closed_ports.append((port_num, service))
        else:
            print(f"\n[!] Port {port_num}/{service}: {status}")
        
    #display summary of number of ports
    print("-" * 50)
    print(f"\n[*] Scan completed at {datetime.now().strftime('%y-%m-%d %H:%M:%S')}")
    print(f"\n[*] Open ports: {len(open_ports)}")
    print(f"\n[*] Closed ports: {len(closed_ports)}")

    #displaying only the open ports
    if open_ports:
        print("\n[+] Open ports found: ")
        for port, service in open_ports:
            print(f"    {port}/{service}")

#scan list of common ports with servie names
def scan_common_ports(target):
    ports = list(COMMMON_PORTS.keys())
    print(f"\n[*] Scanning common ports on {target}...")
    scan_multiple_ports(target, ports)

#validation allows for clear error message
def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def main():
    print("=" * 50)
    print("Python Port Scanner")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("1. Scan a single port")
        print("2. Scan multiple ports")
        print("3. Scan common ports")
        print("4. Exit") #loop runs infinitely until user chooses to exit

        choice = input("\nSelect option (1-4): ")

        if choice == "1":
            target = input("Enter an IP address: ")
            if not validate_ip(target): #calling validate_ip function
                print("[!] The IP address is invalid.")
                continue

            try:
                port = int(input("Enter a port number (1-65535): "))
                if not 1 <= port <= 65535:
                    print("[!] Port number is invalid. Must be between 1 and 65535.")
                    continue
                scan_single_port(target, port)
            except ValueError:
                print("[!] Invalid port format")
                continue

        elif choice == "2":
            target = input("Please enter an IP address: ")
            if not validate_ip(target):
                print("[!] The IP address is invalid.")
                continue

            port_input = input("Enter the port numbers (comma-sperated, e.g. 25, 80): ")
            try:
                ports = [int(p.strip()) for p in port_input.split(",")]
                if not all(1 <= p <= 65535 for p in ports):
                    print("[!] One or more port numbers are invalid. Must be between 1 and 65535.")
                    continue
                scan_multiple_ports(target, ports)
            except ValueError:
                print("[!] Invalid port format")
                continue


            
        elif choice == "3":
            target = input("Please enter an IP address: ")
            if not validate_ip(target):
                print("[!] IP address is invalid.")
                continue

            scan_common_ports(target)

        elif choice == "4":
            print("Exiting Port Scanner. Bye!")
            sys.exit(0)
        
        else:
            print("[!] Invalid option. Please select options 1-4.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Scan interrupted by user. Exiting...")
        sys.exit(0)