### analyze failed logins

### open and read the log file
with open("auth_log.txt", "r") as file:
    auth_log = file.read()

### split file into a list
auth_log = auth_log.split("\n")

### create empty dictionary
failed_logins = {}

### counter for malformed entries
malformed_entries = 0

### add users to dictionary
for event in auth_log:
    split_event = event.split()
    ### checks if event contains expected number of fields
    if len(split_event) == 4:
         ### if user not in dictionary and event failed, add user to dictionary 
        if split_event[2] not in failed_logins and split_event[3].upper() == "FAILED":
            failed_logins[split_event[2]] = 0
        ### added failed occurence to dictionary
        if split_event[3].upper() == "FAILED":
            failed_logins[split_event[2]] = failed_logins[split_event[2]] + 1 
    ### ignore empty lines
    elif len(split_event) == 0:
        continue
    ### counts malformed entries if not 4 fields
    else: 
        malformed_entries = malformed_entries + 1


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

### spacing for malformed number
print("")
### print malformed number
print("Malformed events:", malformed_entries)