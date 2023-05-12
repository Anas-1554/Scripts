#!/usr/bin/python3

import requests
import json
import argparse
import socket
from sty import fg, bg, ef, rs

# Set your API token here
API_TOKEN = '<BSDK Khud ki token dal>'

def print_colored(text, color):
    """
    Prints the given text in the given color.
    """
    print(color + text + fg.rs)


def main():
    parser = argparse.ArgumentParser(description='Get IP address information')
    parser.add_argument('ip_or_domain', metavar='IP or Domain', type=str, help='IP address or Domain name')
    args = parser.parse_args()

    ip_or_domain = args.ip_or_domain

    try:
        # Check if IP address or domain name was passed
        socket.inet_aton(ip_or_domain)
        ip_address = ip_or_domain
    except OSError:
        try:
            # Resolve domain name to IP address
            ip_address = socket.gethostbyname(ip_or_domain)
        except socket.gaierror:
            print_colored('Invalid IP or domain name', fg.red)
            return

    url = f'https://ipinfo.io/{ip_address}?token={API_TOKEN}'
    response = requests.get(url)

    # Parse JSON response
    data = json.loads(response.text)

    # Print IP address information with colors and styles
    print(fg.green + 'IP address:' + fg.yellow, data['ip'])
    print("\n")
    print(fg.green + 'Organization:' + fg.cyan, data['org'])
    if 'hostname' in data:
     print(fg.green + 'Hostname:' + fg.rs, data['hostname']) 
    print("\n")
    print(fg.green + 'Country:' + fg.rs, data['country'])
    print(fg.green + 'Region:' + fg.rs, data['region'])
    print(fg.green + 'City:' + fg.rs, data['city'])
    print("\n")
    print(fg.green + 'Location:' + fg.rs, data['loc'])

if __name__ == '__main__':
    main()
