# CIP ( Check IP Information)

This Python script can be used to fetch information about an IP address or a domain name. It uses the `ipinfo.io` API to get the information and prints it in a nice colored format using the sty library.

## Requirements

1. Python 3.x
2. requests and sty libraries installed (can be installed via pip)

### Usage
```bash 
python ip_info.py <IP or Domain>
```

The script takes one argument, which can be either an IP address or a domain name.

### API Token
The API_TOKEN variable at the top of the script should be set to your own ipinfo.io API token. You can get a token by signing up at https://ipinfo.io/signup.

### Output
The script outputs the following information about the IP address or domain name:
```bash
IP address
Organization (if available)
Hostname (if available)
Country
Region
City
Location (latitude and longitude)```
The information is printed in a nicely formatted and colored output.

Example
bash
Copy code
python ip_info.py google.com
Output:

yaml
Copy code
IP address: 142.251.33.206

Organization: AS15169 Google LLC
Hostname: fra16s32-in-f14.1e100.net

Country: DE
Region: Hesse
City: Frankfurt am Main

Location: 50.1212,8.6366
Credits
The requests library: https://requests.readthedocs.io/en/master/
The sty library: https://sty.mewo.dev/
The ipinfo.io API: https://ipinfo.io/
