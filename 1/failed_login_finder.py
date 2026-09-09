### find failed auth events

### import and read file
with open("auth_log.txt", "r") as file:
    auth_log = file.read()

### split into list
auth_log = auth_log.split("\n")

### examine each entry
for event in auth_log:
    ### print the event if it failed
    if "failed".upper() in event:
        print(event)
