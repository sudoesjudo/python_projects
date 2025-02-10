#  Initial list of IP addresses:
print()
ip_addr_list = ['192.168.1.1', '192.168.2.2', '192.168.3.3', '192.168.4.4', '192.168.5.5']

print("Here is your initial list:\n")
print("\n".join(ip_addr_list))
print()

ip_addr_list.append('192.168.6.6')
ip_addr_list.extend(['192.168.7.7', '192.168.8.8'])
new_ip_list = ip_addr_list + ['192.168.9.9', '192.168.10.10']

print("Here is the updated list:\n")
print("\n".join(new_ip_list))

print("\nHere is the first IP in the list:\n")
print(new_ip_list[0])

print("\nHere is the last IP in the list:\n")
print(new_ip_list[-1] + "\n")

first_ip = new_ip_list.pop(0)
last_ip = new_ip_list.pop(-1)

first_ip = "2.2.2.2"

new_list = [first_ip, last_ip]

print(f"You've changed the first entry in the list.\n")

print(f"Updated Element from {ip_addr_list[0]} to {new_list[0]}\n")

print(f"Here's your new short list\n\n{"\n".join(new_list)}\n")
