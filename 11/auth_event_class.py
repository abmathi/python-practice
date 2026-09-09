### Auth Event Classifier
### classify events by severity level
### high, medium, low

# sus ips
watchlist = [
    "203.0.113.42",
    "198.51.100.17"
]

# auth events
events = [
    ["alice", "SUCCESS", "192.168.1.15"],
    ["bob", "FAILED", "203.0.113.42"],
    ["charlie", "FAILED", "192.168.1.22"],
    ["david", "SUCCESS", "198.51.100.17"],
    ["eve", "FAILED", "198.51.100.17"]
]

# fucntion that checks severity level
# depending on status and ip
def classify_event(status, ip_address):
    
    if status == "FAILED" and ip_address in watchlist:
        severity = "HIGH"
    elif status == "FAILED":
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return severity

# print report title
print("Authentication Event Report")

# print severity report
for event in events:
    print(event[0], "-", classify_event(event[1],event[2]))