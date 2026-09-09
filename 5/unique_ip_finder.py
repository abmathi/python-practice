### unique id finder

### open the auth log file and save as variable
with open("auth_log.txt", "r") as file:
    auth_file = file.read()

### split file into list
auth_file = auth_file.split("\n")

### create empty list 
unique_ips = []

### add ip to list if not in list and event failed
for event in auth_file:
    split_log = event.split()
    if split_log[4] == "FAILED" and split_log[3] not in unique_ips:
        unique_ips.append(split_log[3])

### print report title
print("Suspicious IP Report")

### print listed ips
for ip in unique_ips:
    print(ip)