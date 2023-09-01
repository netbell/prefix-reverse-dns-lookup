import ipaddress
import socket

def reverse_dns(ip_address):
    try:
        return socket.gethostbyaddr(str(ip_address))[0]
    except socket.herror:
        return None

def reverse_dns_for_prefix(prefix, print_all):
    network = ipaddress.ip_network(prefix)
    for ip in network:
        domain_name = reverse_dns(ip)
        if domain_name:
            print(f"{str(ip).ljust(15)} -> {domain_name}")
        if not domain_name and print_all:
            print(f"{str(ip).ljust(15)} -> Not resolved")

if __name__ == '__main__':
    prefix = input("Enter the prefix (e.g. 192.0.2.0/24): ")
    
    choice = input("Print all attempts or just successful resolutions? (all/successful): ").strip().lower()
    if choice.startswith('a'):
        print_all = True
    elif choice.startswith('s'):
        print_all = False
    else:
        print("Invalid choice. Defaulting to printing all attempts.")
        print_all = True
    
    reverse_dns_for_prefix(prefix, print_all)