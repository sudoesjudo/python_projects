# Open the file
with open("show_ip_int_brief.txt", mode="r") as f:
    data = f.readlines() #  Read the file

    for line in data: #  Loop the file
        if "10.220" in line: #  Print the line if the string is found
            line_list = line.split() #  Split by space and convert to list
            intf_name = line_list[0] #  Assign coloumn 1 to intf_name
            ip_addr = line_list[1] #  Assign coloumn 2 to ip_addr
            print(f"\nInterface: {intf_name}\nIP Address: {ip_addr}\n") #  If "10.220.", print interface name and IP
