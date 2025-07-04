import pprint as p

contacts = {}
def save_contact():
    for i in range(int(input("Number of contacts to be saved: "))):
        name = input("Name: ")
        contacts[name] = {}
        contacts[name]["phone"] = input("Phone: ")
        contacts[name]["email"] = input("Email: ")
        print(f"Contact {i+1} Details")


def search_contact(name):
    if name in contacts.keys():
        p.pprint(contacts[name])
    else:
        print("Not found")


# p.pprint(contacts)
while(True):
    val = int(input("1. Save Contacts\n2. Search Contact\n3. Exit\nEnter an option: "))
    if val == 1:
        save_contact()
    elif val == 2:
        search_contact(input("Name: "))
    else:
        break
