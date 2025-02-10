# Base Addressing
base_addr = "192.168.254."

print()

while True:
    try:
        #  Prompt for user input
        prefix_len = int(input("Please input a prefix length between 25 and 30: "))

        if 25 <= prefix_len <= 30:

            #  Variables and conditional output
            hosts_avail = 2**(32-prefix_len) - 2
            first_addr = 1
            last_addr = hosts_avail
            broadcast_addr = hosts_avail +1
            subnet_block = 2**(32-prefix_len)
            second_network = base_addr + str(subnet_block)
            #  Calculates the last octect for the subnet mask based on the entered prefix length
            last_octet = 256-2**(32-prefix_len)
            netmask = f"255.255.255.{last_octet}"

            #  Show the preflix link to netmask conversion and print the result
            print("\n"+ f"The /{prefix_len} is a valid subnet within the expected range.")
            print(f"I went ahead and converted your prefix into a subnet mask:\n{netmask}\n")

            #  Final output if program runs to completion without any invalid input
            print(f"Your first Network address is {base_addr}0.\n")
            print(f"You have {hosts_avail} available IP addresses to assign.\n")
            print(f"The first and last available addresses in the /{prefix_len} subnet are:\n")
            print(f"First valid Host IP Address: {base_addr}{first_addr}")
            print(f"Last valid Host IP: {base_addr}{last_addr}\n")
            print(f"Broadcast: {base_addr}{broadcast_addr}\n")
            print(f"The next network available given a block size of {subnet_block} and a /{prefix_len} is {second_network}")
            print()
            break  # Exit loop if valid

        #  If invalid:
        print("\nInvalid input! Value must be no less than 25 and no greater than 30.\n")

    #  In case a letter or non-number was entered:
    except ValueError:
        print("\nInput must be an integer. Please try again.\n")
