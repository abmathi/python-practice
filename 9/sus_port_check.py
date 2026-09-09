### function that checks for ports that team flagged as suspicious
### 21, 23, 3389 are flagged ports

### define the function 
### if ports equal to flagged ports. return true
### else return false
def check_port(port_number):
    if port_number == 21:
        return True
    elif port_number == 23:
        return True
    elif port_number == 3389:
        return True
    else: 
        return False


### list of ports to loop through
ports = [22, 23, 80, 443, 3389, 8080, 21]

### loop through ports with function
### if function returns true, print alert
for port in ports:
    if check_port(port):
        print("ALERT: Port", port, "requires review")