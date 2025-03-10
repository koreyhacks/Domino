#!/usr/bin/env python3
"""
Domino - Domain Enumeration Tool for Ethical Hacking
---------------------------------------------------
A Python tool to perform reconnaissance on domains by gathering information
through DNS queries, subdomain enumeration, and basic service discovery.
"""

import argparse
import socket
import dns.resolver
import whois
import requests
import concurrent.futures
from colorama import Fore, Style, init
from tqdm import tqdm

# Initialize colorama
init()

class Domino:
    def __init__(self, domain, threads=10, timeout=5, verbose=False):
        self.domain = domain
        self.threads = threads
        self.timeout = timeout
        self.verbose = verbose
        self.subdomains = set()
        self.dns_records = {}
        self.open_ports = {}
        
    def print_banner(self):
        """Print a tool banner"""
        banner = f"""
{Fore.WHITE}██████╗  ██████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
{Fore.WHITE}██╔══██╗██╔═══██╗████╗ ████║██║████╗  ██║██╔═══██╗
{Fore.RED}██║  ██║██║   ██║██╔████╔██║██║██╔██╗ ██║██║   ██║
{Fore.RED}██║  ██║██║   ██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
{Fore.CYAN}██████╔╝╚██████╔╝██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
{Fore.CYAN}╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                 
{Fore.WHITE}╔═══════════════════════════════════════════════════╗
{Fore.WHITE}║ {Fore.CYAN}Domain Reconnaissance & Enumeration Tool {Fore.RED}v1.0{Fore.WHITE}   ║
{Fore.WHITE}║ {Fore.YELLOW}By koreyhacks_{Fore.WHITE}                                 ║
{Fore.WHITE}╚═══════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)
        print(f"{Fore.GREEN}[*] Target domain: {Fore.WHITE}{self.domain}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[*] Threads: {Fore.WHITE}{self.threads}{Style.RESET_ALL}")
        print()
        
    def get_ip_address(self):
        """Get the IP address for the main domain"""
        try:
            ip = socket.gethostbyname(self.domain)
            print(f"{Fore.GREEN}[+] IP Address for {self.domain}: {Fore.WHITE}{ip}{Style.RESET_ALL}")
            return ip
        except socket.gaierror:
            print(f"{Fore.RED}[-] Could not resolve IP for {self.domain}{Style.RESET_ALL}")
            return None
            
    def get_whois_info(self):
        """Get WHOIS information for the domain"""
        try:
            w = whois.whois(self.domain)
            print(f"\n{Fore.CYAN}[+] WHOIS Information:{Style.RESET_ALL}")
            print(f"    {Fore.GREEN}Registrar: {Fore.WHITE}{w.registrar}{Style.RESET_ALL}")
            print(f"    {Fore.GREEN}Creation Date: {Fore.WHITE}{w.creation_date}{Style.RESET_ALL}")
            print(f"    {Fore.GREEN}Expiration Date: {Fore.WHITE}{w.expiration_date}{Style.RESET_ALL}")
            if w.name_servers:
                print(f"    {Fore.GREEN}Name Servers: {Fore.WHITE}{', '.join(w.name_servers) if isinstance(w.name_servers, list) else w.name_servers}{Style.RESET_ALL}")
            return w
        except Exception as e:
            print(f"{Fore.RED}[-] Could not get WHOIS info: {str(e)}{Style.RESET_ALL}")
            return None
            
    def get_dns_records(self, record_types=None):
        """Get DNS records for the domain"""
        if record_types is None:
            record_types = ['A', 'AAAA', 'NS', 'MX', 'TXT', 'SOA', 'CNAME']
        
        print(f"\n{Fore.CYAN}[+] DNS Records:{Style.RESET_ALL}")
        
        for record_type in record_types:
            try:
                answers = dns.resolver.resolve(self.domain, record_type)
                self.dns_records[record_type] = [str(rdata) for rdata in answers]
                
                print(f"    {Fore.GREEN}{record_type} Records:{Style.RESET_ALL}")
                for rdata in answers:
                    print(f"        {Fore.WHITE}{rdata}{Style.RESET_ALL}")
            except Exception as e:
                if self.verbose:
                    print(f"    {Fore.RED}[-] No {record_type} Records: {str(e)}{Style.RESET_ALL}")
        
        return self.dns_records
    
    def enumerate_subdomains(self, wordlist_file):
        """Enumerate subdomains using a wordlist file"""
        try:
            with open(wordlist_file, 'r') as f:
                wordlist = [line.strip() for line in f]
        except FileNotFoundError:
            print(f"{Fore.RED}[-] Wordlist file not found: {wordlist_file}{Style.RESET_ALL}")
            return []
            
        print(f"\n{Fore.CYAN}[+] Enumerating subdomains using wordlist ({len(wordlist)} words)...{Style.RESET_ALL}")
        
        found_subdomains = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            future_to_subdomain = {
                executor.submit(self._check_subdomain, f"{word}.{self.domain}"): word 
                for word in wordlist
            }
            
            for future in tqdm(concurrent.futures.as_completed(future_to_subdomain), 
                               total=len(wordlist), 
                               desc="Progress", 
                               unit="subdomain"):
                subdomain = future_to_subdomain[future]
                try:
                    result = future.result()
                    if result:
                        found_subdomain = f"{subdomain}.{self.domain}"
                        found_subdomains.append(found_subdomain)
                        ip = result
                        print(f"    {Fore.GREEN}[+] Found: {Fore.WHITE}{found_subdomain} ({ip}){Style.RESET_ALL}")
                except Exception as e:
                    if self.verbose:
                        print(f"    {Fore.RED}[-] Error checking {subdomain}.{self.domain}: {str(e)}{Style.RESET_ALL}")
        
        print(f"\n{Fore.GREEN}[+] Found {len(found_subdomains)} subdomains{Style.RESET_ALL}")
        return found_subdomains
    
    def _check_subdomain(self, subdomain):
        """Check if a subdomain exists by resolving it"""
        try:
            ip = socket.gethostbyname(subdomain)
            self.subdomains.add(subdomain)
            return ip
        except socket.gaierror:
            return False
            
    def check_common_ports(self, ip, ports=None):
        """Check for open ports on the target IP"""
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
            
        print(f"\n{Fore.CYAN}[+] Checking common ports on {ip}...{Style.RESET_ALL}")
        
        open_ports = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            future_to_port = {
                executor.submit(self._check_port, ip, port): port for port in ports
            }
            
            for future in tqdm(concurrent.futures.as_completed(future_to_port), 
                              total=len(ports), 
                              desc="Progress", 
                              unit="port"):
                port = future_to_port[future]
                try:
                    is_open = future.result()
                    if is_open:
                        open_ports.append(port)
                        service = socket.getservbyport(port) if port < 1024 else "unknown"
                        print(f"    {Fore.GREEN}[+] Port {port} ({service}): {Fore.WHITE}Open{Style.RESET_ALL}")
                except Exception as e:
                    if self.verbose:
                        print(f"    {Fore.RED}[-] Error checking port {port}: {str(e)}{Style.RESET_ALL}")
        
        self.open_ports[ip] = open_ports
        return open_ports
    
    def _check_port(self, ip, port):
        """Check if a port is open"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        
        try:
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            sock.close()
            return False
    
    def check_web_server(self, url=None):
        """Check for web server and get HTTP headers"""
        if url is None:
            urls = [f"http://{self.domain}", f"https://{self.domain}"]
        else:
            urls = [url]
            
        print(f"\n{Fore.CYAN}[+] Checking web servers...{Style.RESET_ALL}")
        
        for url in urls:
            try:
                response = requests.get(url, timeout=self.timeout, allow_redirects=False)
                print(f"    {Fore.GREEN}[+] {url}: {Fore.WHITE}Status {response.status_code}{Style.RESET_ALL}")
                
                # Get headers
                print(f"    {Fore.GREEN}[+] HTTP Headers:{Style.RESET_ALL}")
                for header, value in response.headers.items():
                    print(f"        {Fore.GREEN}{header}: {Fore.WHITE}{value}{Style.RESET_ALL}")
                    
                # Check for security headers
                security_headers = [
                    'Strict-Transport-Security',
                    'Content-Security-Policy',
                    'X-Content-Type-Options',
                    'X-Frame-Options',
                    'X-XSS-Protection'
                ]
                
                missing_headers = [h for h in security_headers if h not in response.headers]
                if missing_headers:
                    print(f"    {Fore.YELLOW}[!] Missing security headers: {Fore.WHITE}{', '.join(missing_headers)}{Style.RESET_ALL}")
                
            except requests.exceptions.SSLError:
                print(f"    {Fore.RED}[-] {url}: SSL Error{Style.RESET_ALL}")
            except requests.exceptions.ConnectionError:
                print(f"    {Fore.RED}[-] {url}: Connection Error{Style.RESET_ALL}")
            except requests.exceptions.Timeout:
                print(f"    {Fore.RED}[-] {url}: Connection Timeout{Style.RESET_ALL}")
            except Exception as e:
                print(f"    {Fore.RED}[-] {url}: {str(e)}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description='Domino - Domain Enumeration Tool for Ethical Hacking')
    parser.add_argument('domain', help='Target domain to enumerate')
    parser.add_argument('-w', '--wordlist', help='Wordlist file for subdomain enumeration')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of threads to use (default: 10)')
    parser.add_argument('-to', '--timeout', type=int, default=5, help='Timeout for connections in seconds (default: 5)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    
    args = parser.parse_args()
    
    enumerator = Domino(args.domain, args.threads, args.timeout, args.verbose)
    enumerator.print_banner()
    
    # Get basic information
    ip = enumerator.get_ip_address()
    enumerator.get_whois_info()
    enumerator.get_dns_records()
    
    # Check for web servers
    enumerator.check_web_server()
    
    # Check for open ports if we have an IP
    if ip:
        enumerator.check_common_ports(ip)
    
    # Enumerate subdomains if wordlist is provided
    if args.wordlist:
        subdomains = enumerator.enumerate_subdomains(args.wordlist)
    
    print(f"\n{Fore.CYAN}[+] Enumeration complete for {args.domain}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
