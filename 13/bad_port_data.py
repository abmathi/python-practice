### handle bad port data
### turn strings to integers
### handle value error

### list of ports
ports = [
    "22",
    "443",
    "not-a-port",
    "3389",
    "80",
    "unknown",
    "8080"
]

### loop through ports list
for port in ports:
    ### try to turn string to integer
    ### print valid port number
    try:
         port_number = int(port)
         print("Valid port:", port_number)
    ### handle value errors for non numbers
    except ValueError:
         ### print invalid port
         print("Invalid port:", port)