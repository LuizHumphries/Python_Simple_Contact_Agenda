from typing import Union, List, Dict

#Type
Contact = Dict[str, Union[str, bool]]
Contacts = List[Contact]
Favorites = List[Contact]

# Functions
def add_contact(contacts: Contacts, contact: Contact) -> None:
    contact = {"Name": contact["Name"], "Phone": contact["Phone"], "Email": contact["Email"], "Favorite": contact["Favorite"]}
    contacts.append(contact)

def see_full_contact_list(contacts: Contacts) -> None:
    print("\nContact List:")
    for count, contact in enumerate(contacts, start = 1):
        contact_name = contact["Name"]
        contact_phone = contact["Phone"]
        contact_email = contact["Email"]
        favorite_status = "🌟" if contact["Favorite"] else " "
        print(f"> {count}. [{favorite_status}] {contact_name} | {contact_phone} | {contact_email}")


    

# Lists
favorites = []
contacts= []



while True:
    print("""\nTask Manager Menu:
    1. Add contact
    2. See favorite contacts list
    3. See all contacts
    4. Update contact
    5. Add contact as favorite
    6. Remove contact as favorite
    7. Quit""")




    contact_list_options = input("Select your option: ")

    if contact_list_options == "1":
        new_contact_name = input("What is the contact name? ")
        if new_contact_name:
            new_contact_phone = input("What is the contact phone number? ")
            new_contact_email = input("What is the contact email? ")
            new_contact = {"Name": new_contact_name, "Phone": new_contact_phone, "Email": new_contact_email, "Favorite": False}
            add_contact(contacts, new_contact)
        else:
            print("You cant create a new contact without the Name")
    elif contact_list_options == "3":
        see_full_contact_list(contacts)
    elif contact_list_options == "7":
        break
    else:
        print("\nOption invalid!")
