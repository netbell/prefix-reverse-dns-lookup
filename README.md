[![Tests](https://github.com/netbell/prefix-reverse-dns-lookup/actions/workflows/tests.yml/badge.svg)](https://github.com/netbell/prefix-reverse-dns-lookup/actions/workflows/tests.yml)

# IP Prefix Reverse DNS Lookup
This code performs reverse DNS lookups for all IP addresses within a given IP prefix.

## Requirements
- Python 3
- dnspython library: Install via pip with `pip install dnspython`.

## Usage
1. Clone the repository:
```
git clone https://github.com/netbell/prefix-reverse-dns-lookup.git
cd src/prefix-reverse-dns-lookup/
```

### Interactive
2. Run the script:
```
python3 prefix_reverse_dns_lookup.py
```

3. Enter the desired IP prefix (e.g., 192.0.2.0/24).

4. Choose whether you'd like to:
 - Print all lookup attempts
 - Only display successful resolutions

### Command Line
2. Run the script:
```
python3 prefix_reverse_dns_lookup.py
```

3. Supply command line arguments

- --prefix: The IP prefix in CIDR notation you wish to scan, e.g., `192.168.1.0/24`.
- --print: Choose the results to print. Use `all` to print all lookup attempts or `successful` to only print IPs with successful resolutions. Defaults to `all`.
- --dns-server: Specify the DNS server's IP for resolution. Defaults to `1.1.1.1`.

#### Example:
To perform a reverse DNS lookup on the prefix 192.168.1.0/24 and print only successful resolutions using the DNS server 8.8.8.8:

```
python prefix_reverse_dns_lookup.py --prefix 192.168.1.0/24 --print successful --dns-server 8.8.8.8
```

If you do not provide command-line arguments, the program will prompt you to input them interactively.

The script will then display the reverse DNS results for each IP address in the specified prefix.

## Features
- Supports both IPv4 and IPv6 prefixes.
- Allows users to select whether all lookup attempts should be displayed or only successful resolutions.
- Aligns IP address output for easy reading.

## Issues and Contributions
For any issues or if you'd like to contribute to the project, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.