import requests
import os
from pathlib import Path
import datetime
from time import sleep

# Links
# Malware: https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt
# Fraud: https://blocklistproject.github.io/Lists/alt-version/fraud-nl.txt
# Scam: https://raw.githubusercontent.com/elliotwutingfeng/GlobalAntiScamOrg-blocklist/main/global-anti-scam-org-scam-urls-pihole.txt
# Bitcoin mining: https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt
# Phishing: https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt
# Ransomware: https://blocklistproject.github.io/Lists/alt-version/ransomware-nl.txt
# Ads + Tracking: https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt
# Fake news: https://github.com/StevenBlack/hosts/blob/master/alternates/fakenews-only/hosts
# Clickbait: https://raw.githubusercontent.com/infinitytec/blocklists/master/clickbait.txt



links = {
    "Malware": "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt",
    "Fraud": "https://blocklistproject.github.io/Lists/alt-version/fraud-nl.txt",
    "Scam": "https://raw.githubusercontent.com/elliotwutingfeng/GlobalAntiScamOrg-blocklist/main/global-anti-scam-org-scam-urls-pihole.txt",
    "Bitcoin mining": "https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt",
    "Phishing": "https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt",
    "Ransomware": "https://blocklistproject.github.io/Lists/alt-version/ransomware-nl.txt",
    "Ads + Tracking": "https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt",
    "Fake news": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-only/hosts",
    "Clickbait": "https://raw.githubusercontent.com/infinitytec/blocklists/master/clickbait.txt"
}

stored = []

def append_hosts(name, url):
    response = requests.get(url)

    if response.status_code == 200:

        with open("hosts", "a", encoding="utf-8") as f:
            f.write(response.text + "\n")
        print(f"{name} appended successfully.")
        stored.append(name)

    else:
        print(f"Failed to fetch {name}: {response.status_code}")

def main():
    print("Host Manager")
    sleep(0.1)
    print(f"Currently stored: {stored}")

    host_selection = input(
        "Select a host file to manage:\n"
        "(1) Malware | "
        "(2) Fraud | "
        "(3) Scam | "
        "(4) Bitcoin mining | "
        "(5) Phishing | "
        "(6) Ransomware |"
        "(7) Ads + Tracking | "
        "(8) Fake news | "
        "(9) Clickbait | "
        "(10) Clear | "
        "(11) Apply stored | "
        "(12) Exit:\n"
    )

    if host_selection == "1":
        append_hosts("Malware", links["Malware"])

    elif host_selection == "2":
        append_hosts("Fraud", links["Fraud"])

    elif host_selection == "3":
        append_hosts("Scam", links["Scam"])

    elif host_selection == "4":
        append_hosts("Bitcoin mining", links["Bitcoin mining"])

    elif host_selection == "5":
        append_hosts("Phishing", links["Phishing"])

    elif host_selection == "6":
        append_hosts("Ransomware", links["Ransomware"])

    elif host_selection == "7":
        append_hosts("Ads + Tracking", links["Ads + Tracking"])

    elif host_selection == "8":
        append_hosts("Fake news", links["Fake news"])

    elif host_selection == "9":
        append_hosts("Clickbait", links["Clickbait"])

    elif host_selection == "10":
        open("hosts", "w").close()
        stored.clear
        print("Cleared hosts file.")

    elif host_selection == "11":
        pass

    elif host_selection == "12":
        print("Exiting...")
        raise SystemExit
    
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    while True:
        main()
        sleep(1)
