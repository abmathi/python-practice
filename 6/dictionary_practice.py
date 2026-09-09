### sample dictionary
failed_logins = {
    "alice": 2,
    "bob": 5,
    "charlie": 1
}

### bobs current failed logins
print(failed_logins["bob"])

### increase alice value
failed_logins["alice"] = failed_logins["alice"] + 1

### add david to the dictionary
failed_logins["david"] = 1

### report title
print("Failed Login Report")

### loop through the dictionary
for entry in failed_logins:
    print(entry, "-", failed_logins[entry])
