#  Open and read file "show_arp.txt":
with open("show_arp.txt", mode="r") as f:
    show_arp = f.readlines() #  Assigned the contents of show_arp.txt to a variable show_arp
    print("\nThe File Type of show_arp.txt is:")
    print(type(show_arp)) #  Prints the file type
    print("\nThe Length of the file show_arp.txt is:")
    print(len(show_arp)) #  Prints the length of the file
    print(f"\nHere's the first line, or header rather:\n{show_arp[0]}")
    print(f"\n{show_arp[1]}{show_arp[-1]}\n") #  Prints the first and last line of show_arp

    fields = show_arp[0].split() #  Assigns the contents of the header line to a list 'fields'
    print("Here is the new list of fields:")
    print(f"{fields}\n") #  Prints the list 'fields'
    print("Here is the type:")
    print(type(fields)) #  Prints the type of 'fields'
    print("\nHere is the length:")
    print(len(fields)) #  Prints the length of 'fields'
    print("\nHere are the first and last fields in fields:")
    print(f"1st: {fields[0]}\nLast: {fields[-1]}\n") #  Prints the first and last elements in 'fields'

#  Context manager .close()
