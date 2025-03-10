# Domino

![image](https://github.com/user-attachments/assets/72793681-9c97-4261-a0d3-1e2cbd547ff8)

Overview
<br>
Domino is a comprehensive domain enumeration tool designed for ethical hackers, penetration testers, and security researchers. This tool streamlines the reconnaissance phase by automating the discovery and analysis of domain information. Domino provides a clean, colorful interface with efficient multi-threaded operations for rapid information gathering.

Features:
<br>
🔍 Domain IP Resolution - Identify the IP address for the target domain
<br>
📋 WHOIS Lookup - Gather domain registration information and metadata
<br>
🌐 DNS Record Analysis - Collect various DNS records (A, AAAA, MX, NS, TXT, etc.)
<br>
🔎 Subdomain Enumeration - Discover valid subdomains using custom wordlists
<br>
🚪 Port Scanning - Check for common open ports and identify running services
<br>
🖥️ Web Server Analysis - Examine HTTP headers and identify missing security headers
<br>
🧵 Multi-threaded Operations - Perform faster scans with configurable thread count
<br>
🎨 Colorized Output - Enhanced terminal output for better readability

Installation:
# Clone the repository
<br>
git clone https://github.com/koreyhacks/domino.git
<br>
cd domino

# Install dependencies
<br>
pip install -r requirements.txt
<br>
![image](https://github.com/user-attachments/assets/eeb47baf-433b-40a6-90b6-31266d939e9b)

Requirements:
<br>
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

Usage:
Basic Usage
<br>
![image](https://github.com/user-attachments/assets/805d6f00-2802-4db7-9acf-7b93677a44e8)
<br>
python domino.py example.com (you can also place the target domain IP)

Advanced Usage:
<br>
![image](https://github.com/user-attachments/assets/025234e6-9367-414b-97dc-b58fb0fb26fd)
<br>
python domino.py example.com -w wordlists/subdomains.txt -t 20 -to 3 -v

Command Line Arguments:
<br>
![image](https://github.com/user-attachments/assets/20ec2a72-7cd7-403c-8fb5-511a6b0c7fa7)

Example Output:
<br>
![image](https://github.com/user-attachments/assets/9c7a7726-8287-48e6-aeef-a80155f79b47)

Wordlists:
<br>
For effective subdomain enumeration, you'll need a wordlist. Some recommended resources:
<br>
https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS
<br>
https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056

Legal Disclaimer:
<br>
This tool is provided for educational and ethical testing purposes only. Users are responsible for complying with applicable laws and obtaining proper authorization before conducting security tests. The author assumes no liability for misuse or damage caused by this tool.
