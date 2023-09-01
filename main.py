import ipaddress
import socket

def reverse_dns(ip_address):
   try:
      return socket.gethostbyaddr(str(ip_address))[0]
   except socket.herror:
      return None

def reverse_dns_for_prefix(prefix, print_all):
   network = ipaddress.ip_network(prefix, strict=False)
   for ip in network:
      domain_name = reverse_dns(ip)
      if domain_name:
         print(f"{str(ip).ljust(15)} -> {domain_name}")
      if not domain_name and print_all:
         print(f"{str(ip).ljust(15)} -> Not resolved")

def validate_prefix(prefix):
   """Validates the IP prefix with CIDR notation."""
   try:
      ipaddress.ip_network(prefix, strict=False)
      return True
   except ValueError:
      return False

if __name__ == '__main__':
   prefix = ""
    
   while not validate_prefix(prefix):
      prefix = input("Enter the prefix (e.g. 192.0.2.0/24): ")
      exit(1)

   choice = input("Print all attempts or just successful resolutions? (all/successful): ").strip().lower()
   if choice.lower().startswith('a'):
      print_all = True
   elif choice.lower().startswith('s'):
      print_all = False
   else:
      print("Invalid choice. Defaulting to printing all attempts.")
      print_all = True
    
   reverse_dns_for_prefix(prefix, print_all)