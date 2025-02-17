#  Welcome Message

print("==============================")
print("||                          ||")
print("||      --------------      ||")
print("||      | WELCOME TO |      ||")
print("||      |THE ADVANCED|      ||")
print("||      |   SUBNET   |      ||")
print("||      | CALCULATOR |      ||")
print("||      --------------      ||")
print("||                          ||")
print("==============================")

#  We will build off of this base IP address
base_addr = "192.168.254."
#  While loop to prevent input errors allowing the code to persist
while True:
    try:
        #  Prompt for a prefix length. Number must be an integer no less than 25, no greater than 30
        prefix_len = int(input(f"\nPlease enter a prefix length.\nThe number must be whole and between 25 and 30.\nEnter Number: "))
        if 25 <= prefix_len <= 30: #  Given user input is a whole number between 25-30
            subnet_size = 2**(32 - prefix_len)
            avail_nets = 256 // subnet_size
            hosts_avail = subnet_size - 2
            last_octet = 0
            print(f"\nYour subnet block size is {subnet_size}\n")
            print(f"You have {hosts_avail} host addresses available to assign within each subnet.")
            if prefix_len:
                print(f"\nThere are {avail_nets} networks available to assign.\nNetwork, Broadcast, First, and Last IP Addresses are listed below:\n")
                for last_octet in range(0, 256, subnet_size):
                    print(f"Network Address: {base_addr}{last_octet}\n")

                    broadcast_addr = last_octet + subnet_size - 1
                    print(f"Broadcast Address: {base_addr}{broadcast_addr}\n")

                    first_ip = last_octet + 1
                    print(f"First Usable Address: {base_addr}{first_ip}\n")

                    last_ip = broadcast_addr - 1
                    print(f"Last Usable Address: {base_addr}{last_ip}\n")
                    print("-" * 32 + "\n")

        else:  #  If the number is out of range
            print(f"{prefix_len} is not within the given range.")
            break
    except ValueError: #  If the input is anything other than a number
        print("That is not a valid input.\nPlease enter a whole number between 25 and 30.")
