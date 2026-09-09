### analyze failed logins

### open and read the log file
with open("auth_log.txt", "r") as file:
    auth_log = file.read()

### split file into a list
auth_log = auth_log.split("\n")

### create empty dictionary
failed_logins = {}

### add users to dictionary
for event in auth_log:
    split_event = event.split()
    ### checks if event contains expected number of fields
    if len(split_event) == 4:
         ### check if user in dictionary
        if split_event[2] not in failed_logins:
            failed_logins[split_event[2]] = 0
        ### added failed occurence to dictionary
        if split_event[3].upper() == "FAILED":
            failed_logins[split_event[2]] = failed_logins[split_event[2]] + 1 
          
### print report title
print("Failed Login Report")

### print report
for user in failed_logins:
    print(user, "-", failed_logins[user])

### print report alert
for user in failed_logins:
    if failed_logins[user] >= 5:
        ### spacing for the alert
        print("")
        print("ALERT:", user, "exceeded the failed login threshold!")        
