### pt 1 of refactorting analyze failed logins
### from 8.5

### start turning actions into functions
### first function is to validate events
### second function counts the failed logins

### open and read the log file
with open("auth_log.txt", "r") as file:
    auth_log = file.read()

### split file into a list
auth_log = auth_log.split("\n")

### create empty dictionary
failed_logins = {}

### counter for malformed entries
malformed_entries = 0

### function that checks len of events
def validate_event(split_event):
    if len(split_event) == 4:
        return True
    else:
        return False

### checks if event is failed
### adds user if needed
### increments users count
def count_failed_logins(current_event, failed_dict):
    if current_event[2] not in failed_dict and current_event[3].upper() == "FAILED":
        failed_dict[current_event[2]] = 0

    if current_event[3].upper() == "FAILED":
        failed_dict[current_event[2]] = failed_dict[current_event[2]] + 1

### loop through the log and split
for event in auth_log:
    split_event = event.split()
    ### checks if event is valid
    if validate_event(split_event):
         ### counts the failed logins
        count_failed_logins(split_event, failed_logins)
        
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