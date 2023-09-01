[![Tests](https://github.com/netbell/prefix-reverse-dns-lookup/actions/workflows/tests.yml/badge.svg)](https://github.com/netbell/prefix-reverse-dns-lookup/actions/workflows/tests.yml)

# Prefix Reverse DNS Lookup
This code performs reverse DNS lookups for all IP addresses within a given IP prefix.

## Requirements
Python 3

## Usage
1. Clone the repository:
```
git clone https://github.com/netbell/prefix-reverse-dns-lookup.git
cd prefix-reverse-dns-lookup
```

2. Run the script:
```
python3 prefix_reverse_dns_lookup.py
```

3. Enter the desired IP prefix (e.g., 192.0.2.0/24).

4. Choose whether you'd like to:
 - Print all lookup attempts, or
 - Only display successful resolutions.

The tool will then display the reverse DNS results for each IP address in the specified prefix.

Features
- Supports both IPv4 and IPv6 prefixes.
- Allows users to select whether all lookup attempts should be displayed or only successful resolutions.
- Aligns IP address output for easy reading.

## Issues and Contributions
For any issues or if you'd like to contribute to the project, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.