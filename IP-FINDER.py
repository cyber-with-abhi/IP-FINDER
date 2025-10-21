# IP Finder Tool

import socket

def find_ip():
    hostname = input("Enter a hostname to find its IP address: ")
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"The IP address of {hostname} is {ip_address}")
    except socket.gaierror:
        print("Hostname could not be resolved. Please try again.")

def main():
    while True:
        print("\nOptions:")
        print("1. Find IP address")
        print("2. Exit")
        choice = input("Select an option (1 or 2): ")

        if choice == '1':
            find_ip()
        elif choice == '2':
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1 or 2.")

if __name__ == "__main__":
    main()
    
