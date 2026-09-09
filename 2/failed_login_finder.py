with open("auth_log.txt", "r") as file:
    auth_log = file.read()

### split into list
auth_log = auth_log.split("\n")

### examine each entry
for event in auth_log:
    split_event = event.split()
    if "FAILED" in split_event:
        print(split_event[2])