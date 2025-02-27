# Empty lists for appending later
interfaces = []
ip_addr = []

# Read the file, assign to a var. file
with open("show_ip_int_brief.txt") as file:
    ip_int_br = file.readlines() # Read lines as a list, assign output to a var. ip_int_br

    # Loop over the contents
    for line in ip_int_br:
        columns = line.split() # Split into columns
        if "10." in columns[1]: # Search for lines that contain "10." and append to lists
            interfaces.append(columns[0])
            ip_addr.append(columns[1])

# Print the lists
print("Interfaces with IPs:", interfaces)
print("Corresponding IPs:  ", ip_addr)

