import socket
from datetime import datetime

def getSubsFromFile(filename):
    sub_domains = []
    with open(filename) as file:
        for sub_domain in file:
            sub_domains.append(sub_domain.strip())
    return sub_domains

def scan_domain(sub_domain, target_domain):
    try:
        full_domain = f"{sub_domain}.{target_domain}"
        ip = socket.gethostbyname(full_domain)
        return 0
    except socket.gaierror as e:
        # print(f"{e} for {full_domain}")
        return 1
    
def scan_sub_domains(target_domain):
    print(f"Scanning {target_domain} for sub domains")
    sub_domains = []

    for sub_domain in getSubsFromFile("subdomains-10000.txt"):
        if scan_domain(sub_domain, target_domain) == 0:
            sub_domains.append(sub_domain)
    
    return sub_domains

if __name__ == "__main__":
    target_domain = input("Enter the target domain: ")

    start_time = datetime.now()
    sub_domains = scan_sub_domains(target_domain)

    end_time = datetime.now()
    duration = end_time - start_time
    # print results
    print(f"Scanning completed in {duration}.\n The following sub domains are present:")
    print(*sub_domains)