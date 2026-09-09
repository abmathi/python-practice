### find failed auth events

### import and read file
with open("auth_log.txt", "r") as file:
    auth_log = file.read()

### split into list
auth_log = auth_log.split("\n")

### empty list for suspicious ips
suspicious_ips = []

### examine each entry
for event in auth_log:
    ### split event into another list
    split_event = event.split()
    ### if event failed then append it to a list
    if split_event[4] == "FAILED":
        suspicious_ips.append(split_event[2:4])

### display title of report
print("Failed Login Report")

### print suspicious list
for entry in suspicious_ips:
    print(entry[0], "-", entry[1])

