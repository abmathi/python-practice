### network scan parser
### loop through scan and return port report
### by using try/except
### i tested a few different methods here

### Scan list
scan_results = [
    "192.168.1.10 22 open",
    "192.168.1.15 443 open",
    "MALFORMED",
    "192.168.1.20 unknown closed",
    "192.168.1.25 3389 open",
    "192.168.1.30 80 closed",
    "192.168.1.35 not-a-port open",
    "",
    "192.168.1.40 8080 open"
]

### first function i tested out

# def test(test_event):
#     try:
#         port_number = int(test_event[1])
#         print(test_event[0], "- Port", port_number, "-", test_event[2].upper())
    
#     except ValueError:
#         print("Invalid port:", test_event[1])

### tested turning it all into function ###

def big_test(scan_list):
    for event in scan_list:
        split_event = event.split()
        if len(split_event) == 0:
            continue
        elif len(split_event) < 3:
         print("Malformed entry:", split_event[0])
        else:
            try:
                port_number = int(split_event[1])
                print(split_event[0], "- Port", port_number, "-", split_event[2].upper())

            except ValueError:

                print("Invalid port:", split_event[1])
            
big_test(scan_results)

### original block that handled everything
### then i added a function
### then i tried turning it all into a function above

# for event in scan_results:
#     split_event = event.split()
#     if len(split_event) == 0:
#         continue
#     elif len(split_event) < 3:
#         print("Malformed entry:", split_event[0])
#     else:

        ### added first function ###
#         test(split_event)

    ### before i made the first function ###

#        # try:
#       #     port_number = int(split_event[1])
#        #     print(split_event[0], "- Port", port_number, "-", split_event[2].upper())
#
#        # except ValueError:
#        #     print("Invalid port:", split_event[1])
            