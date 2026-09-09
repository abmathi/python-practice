### Login Risk Score
### assign risk score to login event
### login failed = 2pts
### ip on watchlist = 3pts

### list of sus ips
watchlist = [
    "203.0.113.42",
    "198.51.100.17"
]

### list of login events
events = [
    ["alice", "SUCCESS", "192.168.1.15"],
    ["bob", "FAILED", "203.0.113.42"],
    ["charlie", "FAILED", "192.168.1.22"],
    ["david", "SUCCESS", "198.51.100.17"],
    ["eve", "FAILED", "198.51.100.17"]
]

### function that calculates the score
def calculate_risk(status, ip_address):
    risk_score = 0
    if status == "FAILED":
        risk_score = risk_score + 2
    if ip_address in watchlist:
        risk_score = risk_score + 3
    return risk_score

### print risk title
print("Login Risk Report")

### print the risk report
for event in events:
    print(event[0], "- Risk Score:", calculate_risk(event[1], event[2]))    