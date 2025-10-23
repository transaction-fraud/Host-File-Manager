import requests
import os
# from pathlib import Path
from time import sleep
import shutil

# Links
# All files are provided by the Blocklist Project (https://github.com/blocklistproject/Lists)

# Deceptive: https://blocklistproject.github.io/Lists/abuse.txt
# Ads: https://blocklistproject.github.io/Lists/ads.txt
# Fraud: https://blocklistproject.github.io/Lists/fraud.txt
# Malware: https://blocklistproject.github.io/Lists/malware.txt
# Phishing: https://blocklistproject.github.io/Lists/phishing.txt
# Ransomware: https://blocklistproject.github.io/Lists/ransomware.txt
# Scam: https://blocklistproject.github.io/Lists/scam.txt
# Tracking: https://blocklistproject.github.io/Lists/tracking.txt
# Adobe telemetry: https://blocklistproject.github.io/Lists/adobe.txt

source = "hosts"
destination = "/private/etc"

links = {
    "Abuse": "https://blocklistproject.github.io/Lists/abuse.txt",
    "Ads": "https://blocklistproject.github.io/Lists/ads.txt",
    "Fraud": "https://blocklistproject.github.io/Lists/fraud.txt",
    "Malware": "https://blocklistproject.github.io/Lists/malware.txt",
    "Phishing": "https://blocklistproject.github.io/Lists/phishing.txt",
    "Ransomware": "https://blocklistproject.github.io/Lists/ransomware.txt",
    "Scams": "https://blocklistproject.github.io/Lists/scam.txt",
    "Tracking": "https://blocklistproject.github.io/Lists/tracking.txt" ,
    "Adobe telemetry": "https://blocklistproject.github.io/Lists/adobe.txt"
}



stored = []

def append_hosts(name, url):
    response = requests.get(url)

    if response.status_code == 200:

        with open(source, "a", encoding="utf-8") as f:
            f.write(response.text + "\n")
            f.close()
        print(f"{name} appended successfully.")
        stored.append(name)

    else:
        print(f"Failed to fetch {name}: {response.status_code}")

def main():
    print("Host Manager")
    sleep(0.1)
    print(f"Currently stored: {stored}")

    host_selection = input(
        "Select a host file to add:\n"
        "(1) Abuse | "
        "(2) Ads | "
        "(3) Fraud | "
        "(4) Malware | "
        "(5) Phishing | "
        "(6) Ransomware |"
        "(7) Scams | "
        "(8) Tracking | "
        "(9) Adobe telemetry (BETA) | "
        "(10) Clear | "
        "(11) Apply stored | "
        "(12) Exit:\n>"
    )

    if host_selection == "1":
        append_hosts("Abuse", links["Abuse"])

    elif host_selection == "2":
        append_hosts("Ads", links["Ads"])

    elif host_selection == "3":
        append_hosts("Fraud", links["Fraud"])

    elif host_selection == "4":
        append_hosts("Malware", links["Malware"])

    elif host_selection == "5":
        append_hosts("Phishing", links["Phishing"])

    elif host_selection == "6":
        append_hosts("Ransomware", links["Ransomware"])

    elif host_selection == "7":
        append_hosts("Scams", links["Scams"])

    elif host_selection == "8":
        append_hosts("Tracking", links["Tracking"])

    elif host_selection == "9":
        append_hosts("Adobe telemetry", links["Adobe telemetry"])

    elif host_selection == "10":
        open("hosts", "w").close()
        with open(destination + '/' + source, 'w') as f:
            pass
        with open(destination + '/' + source, 'w') as f:
            f.write('127.0.0.1 localhost\n255.255.255.255 broadcasthost\n::1 localhost')
    
        stored.clear()
        print("Cleared hosts file.")

    elif host_selection == "11":
        if os.path.exists(destination + '/' + source):
            os.remove(destination + '/' + source)
            try:
                shutil.move(source, destination)
            except Exception as e:
                print(f"An exception has occured: {e}")

    elif host_selection == "12":
        print("Exiting...")
        raise SystemExit
    
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    while True:
        main()
        sleep(1)
