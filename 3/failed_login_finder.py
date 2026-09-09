### find failed auth events

### import and read file
with open("auth_log.txt", "r") as file:
    auth_log = file.read()

### split into list
auth_log = auth_log.split("\n")

### count number of fails
fail_count = 0

### examine each entry
for event in auth_log:
    ### split event into another list
    split_event = event.split()
    ### if event failed then counter increases
    if "FAILED" in split_event[3]:
        fail_count = fail_count + 1

### display total failed events
print("Total failed logins:", fail_count)
