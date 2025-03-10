# Domino

![image](https://github.com/user-attachments/assets/72793681-9c97-4261-a0d3-1e2cbd547ff8)

Overview
Domino is a comprehensive domain enumeration tool designed for ethical hackers, penetration testers, and security researchers. This tool streamlines the reconnaissance phase by automating the discovery and analysis of domain information. Domino provides a clean, colorful interface with efficient multi-threaded operations for rapid information gathering.

Features

🔍 Domain IP Resolution - Identify the IP address for the target domain
📋 WHOIS Lookup - Gather domain registration information and metadata
🌐 DNS Record Analysis - Collect various DNS records (A, AAAA, MX, NS, TXT, etc.)
🔎 Subdomain Enumeration - Discover valid subdomains using custom wordlists
🚪 Port Scanning - Check for common open ports and identify running services
🖥️ Web Server Analysis - Examine HTTP headers and identify missing security headers
🧵 Multi-threaded Operations - Perform faster scans with configurable thread count
🎨 Colorized Output - Enhanced terminal output for better readability

Installation
# Clone the repository
git clone https://github.com/koreyhacks/domino.git
cd domino

# Install dependencies
pip install -r requirements.txt

![image](https://github.com/user-attachments/assets/eeb47baf-433b-40a6-90b6-31266d939e9b)

Requirements

Python 3.6+
<br>
dnspython
<br>
python-whois
<br>
requests
<br>
colorama
<br>
tqdm

Usage
Basic Usage

![image](https://github.com/user-attachments/assets/805d6f00-2802-4db7-9acf-7b93677a44e8)
python domino.py example.com (you can also place the target domain IP)

Advanced Usage

![image](https://github.com/user-attachments/assets/025234e6-9367-414b-97dc-b58fb0fb26fd)
python domino.py example.com -w wordlists/subdomains.txt -t 20 -to 3 -v

Command Line Arguments

![image](https://github.com/user-attachments/assets/20ec2a72-7cd7-403c-8fb5-511a6b0c7fa7)

Example Output

![image](https://github.com/user-attachments/assets/9c7a7726-8287-48e6-aeef-a80155f79b47)

Wordlists
For effective subdomain enumeration, you'll need a wordlist. Some recommended resources:
https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS
https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056

Legal Disclaimer
This tool is provided for educational and ethical testing purposes only. Users are responsible for complying with applicable laws and obtaining proper authorization before conducting security tests. The author assumes no liability for misuse or damage caused by this tool.
