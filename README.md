s# DOMINO

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.6+-brightgreen.svg" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<p align="center">
  <b>Domain Reconnaissance & Enumeration Tool</b><br>
  <sub>By koreyhacks_</sub>
</p>

## Overview

Domino is a comprehensive domain enumeration tool designed for ethical hackers, penetration testers, and security researchers. This tool streamlines the reconnaissance phase by automating the discovery and analysis of domain information. Domino provides a clean, colorful interface with efficient multi-threaded operations for rapid information gathering.

![2025-03-10 22_58_03-KALI  Running  - Oracle VirtualBox _ 1](https://github.com/user-attachments/assets/bce3b475-bfbc-4f64-a3ce-0d91719e42de)


## Features

- 🔍 **Domain IP Resolution** - Identify the IP address for the target domain
- 📋 **WHOIS Lookup** - Gather domain registration information and metadata
- 🌐 **DNS Record Analysis** - Collect various DNS records (A, AAAA, MX, NS, TXT, etc.)
- 🔎 **Subdomain Enumeration** - Discover valid subdomains using custom wordlists
- 🚪 **Port Scanning** - Check for common open ports and identify running services
- 🖥️ **Web Server Analysis** - Examine HTTP headers and identify missing security headers
- 🧵 **Multi-threaded Operations** - Perform faster scans with configurable thread count
- 🎨 **Colorized Output** - Enhanced terminal output for better readability

## Installation

```bash
# Clone the repository
git clone https://github.com/koreyhacks/domino.git
cd domino

# Install dependencies
pip install -r requirements.txt
```

### Requirements
- Python 3.6+
- dnspython
- python-whois
- requests
- colorama
- tqdm

## Usage

### Basic Usage

```bash
python domino.py example.com
```

### Advanced Usage

```bash
python domino.py example.com -w wordlists/subdomains.txt -t 20 -to 3 -v
```

### Command Line Arguments

| Argument | Description |
|----------|-------------|
| `domain` | Target domain to enumerate |
| `-w`, `--wordlist` | Wordlist file for subdomain enumeration |
| `-t`, `--threads` | Number of threads to use (default: 10) |
| `-to`, `--timeout` | Timeout for connections in seconds (default: 5) |
| `-v`, `--verbose` | Enable verbose output |

## Example Output

```
██████╗  ██████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██║████╗  ██║██╔═══██╗
██║  ██║██║   ██║██╔████╔██║██║██╔██╗ ██║██║   ██║
██║  ██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                 
╔═══════════════════════════════════════════════════╗
║ Domain Reconnaissance & Enumeration Tool v1.0     ║
║ By koreyhacks_                                    ║
╚═══════════════════════════════════════════════════╝

[*] Target domain: example.com
[*] Threads: 10

[+] IP Address for example.com: 93.184.216.34

[+] WHOIS Information:
    Registrar: RESERVED-Internet Assigned Numbers Authority
    Creation Date: 1995-08-14 04:00:00
    Expiration Date: 2021-08-13 04:00:00
    Name Servers: A.IANA-SERVERS.NET, B.IANA-SERVERS.NET

[+] DNS Records:
    A Records:
        93.184.216.34
    AAAA Records:
        2606:2800:220:1:248:1893:25c8:1946
    NS Records:
        a.iana-servers.net.
        b.iana-servers.net.
    MX Records:
        0 .
    TXT Records:
        v=spf1 -all

[+] Checking web servers...
    [+] http://example.com: Status 200
    [+] HTTP Headers:
        Age: 591744
        Cache-Control: max-age=604800
        Content-Type: text/html; charset=UTF-8
        Date: Wed, 9 Mar 2025 15:03:41 GMT
        Etag: "3147526947"
        Expires: Wed, 16 Mar 2025 15:03:41 GMT
        Last-Modified: Thu, 17 Oct 2024 07:18:26 GMT
        Server: ECS (nyb/1D07)
        Vary: Accept-Encoding
        X-Cache: HIT
        Content-Length: 1256
    [!] Missing security headers: Strict-Transport-Security, Content-Security-Policy, X-Content-Type-Options, X-Frame-Options, X-XSS-Protection

[+] Checking common ports on 93.184.216.34...
    [+] Port 80 (http): Open
    [+] Port 443 (https): Open

[+] Enumeration complete for example.com
```

## Wordlists

For effective subdomain enumeration, you'll need a wordlist. Some recommended resources:

- [SecLists Subdomain Wordlists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS)
- [jhaddix/all.txt](https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056)

## Future Enhancements

- [ ] Certificate transparency log parsing
- [ ] Recursive subdomain enumeration
- [ ] Web screenshots and tech detection
- [ ] Export results (JSON, CSV, HTML)
- [ ] Custom banners and themes
- [ ] API integration (Shodan, Censys, etc.)

## Legal Disclaimer

This tool is provided for educational and ethical testing purposes only. Users are responsible for complying with applicable laws and obtaining proper authorization before conducting security tests. The author assumes no liability for misuse or damage caused by this tool.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Credits

- Created by koreyhacks_
- Inspired by various open-source reconnaissance tools
