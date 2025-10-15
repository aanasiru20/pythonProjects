print("Contact Book")
contactInfo = []
while True: # our while loop start here
    contactLog = input("Address Book (add/show/remove/exit): ").lower()
    if contactLog == "add":
        info = input("Enter a new Contact: ")
        contactInfo.append(info)
        print(info,"has been added")
    elif contactLog == "show":
        print("Contact Log: ")
        for i in contactInfo:
            print("-", i)
    elif contactLog == "remove":
        info = input("Enter the contact you want to remove: ")
        if info in contactInfo:
            contactInfo.remove(info)
            print(info,"removed.")
        else:
            print("Contact not found.")
    elif contactLog == "exit":
        print("Bye!!!")
        break
    else:
        print("Contact Not found.")