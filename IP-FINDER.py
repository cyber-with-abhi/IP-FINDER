import socket

def get_ip_address(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.error as err:
        return f"Error: {err}"

print(f"The IP address of {url} is: {get_ip_address(url)}") 
