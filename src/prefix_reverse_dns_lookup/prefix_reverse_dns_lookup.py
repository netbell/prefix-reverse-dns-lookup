import argparse
import ipaddress
import dns.resolver

DEFAULT_NAMESERVER = '1.1.1.1'

def reverse_dns(ip_address, nameserver):
   resolver = dns.resolver.Resolver(configure=False)
   if nameserver:
      resolver.nameservers = [nameserver]
   
   try:
      answers = resolver.resolve(dns.reversename.from_address(str(ip_address)), 'PTR')
      return str(answers[0])
   except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.exception.Timeout):
      return None


def reverse_dns_for_prefix(prefix, print_all, dns_server):
   network = ipaddress.ip_network(prefix, strict=False)
   for ip in network:
      domain_name = reverse_dns(ip, dns_server)
      if domain_name:
         print(f"{str(ip).ljust(15)} -> {domain_name}")
      elif print_all:
         print(f"{str(ip).ljust(15)} -> Not resolved")


def validate_prefix(prefix):
   """Validates the IP prefix with CIDR notation."""
   try:
      ipaddress.ip_network(prefix, strict=False)
      return True
   except ValueError:
      return False

def parse_args():
   parser = argparse.ArgumentParser(description="Perform a reverse DNS lookup on an IP prefix.")
   
   # IP Prefix
   parser.add_argument("--prefix", type=str, default=None, help="IP prefix to scan (e.g., '192.168.1.0/24').")
   
   # Print all attempts or just successful resolutions
   parser.add_argument("--print", type=str, choices=['all', 'successful'], default='all', dest="print_choice", help="Choose to print all attempts or just successful resolutions.")
   
   # DNS Server
   parser.add_argument("--dns-server", type=str, default=DEFAULT_NAMESERVER, help="Specify the DNS server's IP for resolution.")

   return parser.parse_args()

def main():
   args = parse_args()

   if args.prefix is None or args.print_choice is None:
      prefix = ""
      while not validate_prefix(prefix):
         prefix = input("Enter the prefix (e.g. 192.0.2.0/24): ")

      if args.print_choice is None:
         choice = input("Print all attempts or just successful resolutions? (all/successful): ").strip().lower()
         if choice.startswith('a'):
               print_all = True
         elif choice.startswith('s'):
               print_all = False
         else:
               print("Invalid choice. Defaulting to printing all attempts.")
               print_all = True
      else:
         print_all = True if args.print_choice == "all" else False
   else:
      prefix = args.prefix
      print_all = True if args.print_choice == "all" else False
   
   reverse_dns_for_prefix(prefix, print_all, args.dns_server)

if __name__ == '__main__':
   main()
