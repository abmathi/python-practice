### analyze failed logins

### open and read the log file
with open("auth_log.txt", "r") as file:
    auth_log = file.read()

### split file into a list
auth_log = auth_log.split("\n")

### create empty dictionary
auth_dict = {}

### add users to dictionary
for event in auth_log:
    split_event = event.split()
    auth_dict[split_event[2]] = 0

### add users failed events to dictionary 
for event in auth_log:
    split_event = event.split()

    if split_event[3] == "FAILED":
        auth_dict[split_event[2]] = auth_dict[split_event[2]] + 1
            
### print report title
print("Failed Login Report")

### print report
for user in auth_dict:
    print(user, "-", auth_dict[user])

### print report alert
for user in auth_dict:
    if auth_dict[user] >= 5:
        ### spacing for the alert
        print("")
        print("ALERT:", user, "exceeded the failed login threshold!")        
