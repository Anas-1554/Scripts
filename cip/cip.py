import requests
import json
import argparse
import socket
from tabulate import tabulate
from sty import fg, bg, ef, rs

API_TOKEN = ''

def print_colored(text, color):

    print(color + text + fg.rs)

def remove_protocol(url):
    if url.startswith('http://'):
        return url[len('http://'):]
    elif url.startswith('https://'):
        return url[len('https://'):]
    return url

def get_ip_info(ip_address):
    url = f'https://ipinfo.io/{ip_address}?token={API_TOKEN}'
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = json.loads(response.text)
    return data

def main():
    parser = argparse.ArgumentParser(description='Get IP address information')
    parser.add_argument('ip_or_domain', metavar='IP or Domain', type=str, nargs='+',
                        help='IP address or Domain name')
    parser.add_argument('-t', '--table', action='store_true',
                        help='Display output in a table format')
    args = parser.parse_args()

    ip_or_domains = args.ip_or_domain
    display_table = args.table

    table_headers = ['IP', 'Organization', 'Hostname', 'Country', 'Region', 'City', 'Location']
    table_rows = []

    for ip_or_domain in ip_or_domains:
        ip_or_domain = remove_protocol(ip_or_domain)

        try:
            socket.inet_aton(ip_or_domain)
            ip_addresses = [ip_or_domain]
        except OSError:
            try:
                ip_addresses = [item[4][0] for item in socket.getaddrinfo(ip_or_domain, None)]
            except socket.gaierror:
                print_colored(f'Error retrieving information for {ip_or_domain}', fg.red)
                continue

        for ip_address in ip_addresses:
            data = get_ip_info(ip_address)

            if data is None:
                print_colored(f'Error retrieving information for {ip_address}', fg.red)
                continue

            row = [
                data.get('ip', ''),
                data.get('org', ''),
                data.get('hostname', ''),
                data.get('country', ''),
                data.get('region', ''),
                data.get('city', ''),
                data.get('loc', '')
            ]

            table_rows.append(row)

    if display_table or len(ip_or_domains) == 1:
        print(tabulate(table_rows, headers=table_headers))
    else:
        for row in table_rows:
            print(fg.green + 'IP address:' + fg.yellow, row[0])
            print(fg.green + 'Organization:' + fg.cyan, row[1])
            if row[2]:
                print(fg.green + 'Hostname:' + fg.rs, row[2])
            print(fg.green + 'Country:' + fg.rs, row[3])
            print(fg.green + 'Region:' + fg.rs, row[4])
            print(fg.green + 'City:' + fg.rs, row[5])
            print(fg.green + 'Location:' + fg.rs, row[6])
            print("\n")

if __name__ == '__main__':
    main()
