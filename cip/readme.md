# IP Information Tool

This Python script retrieves information about IP addresses or domain names using the ipinfo.io API. It supports both single and multiple queries and provides the option to display the output in a table format.

## Prerequisites

Before using this script, make sure you have the following requirements installed:

- Python 3.x
- `requests` library (install using `pip install requests`)
- `tabulate` library (install using `pip install tabulate`)
- `sty` library (install using `pip install sty`)

## Usage

To retrieve information for an IP address or domain name, run the script with the following command:

```bash
python ip_info.py [IP or Domain] [-t]
```

Replace `[IP or Domain]` with the IP address or domain name you want to query. You can also provide multiple IP addresses or domain names separated by spaces.

### Optional Arguments

- `-t, --table`: Display output in a table format.

## API Token

To use the ipinfo.io API, you need to set your API token in the `API_TOKEN` variable inside the script. You can obtain an API token by signing up at [ipinfo.io](https://ipinfo.io/).

## Example

Here are a few examples of how to use the script:

- Retrieve information for a single IP address:

  ```bash
  python ip_info.py 8.8.8.8
  ```

- Retrieve information for multiple IP addresses:

  ```bash
  python ip_info.py 8.8.8.8 1.1.1.1 4.4.4.4
  ```

- Retrieve information for a domain name:

  ```bash
  python ip_info.py example.com
  ```

- Retrieve information for multiple domain names:

  ```bash
  python ip_info.py example.com google.com yahoo.com
  ```

- Retrieve information for an IP address and display output in a table format:

  ```bash
  python ip_info.py 8.8.8.8 -t
  ```

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it in your own projects.
