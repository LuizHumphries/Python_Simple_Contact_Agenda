from typing import Union, List, Dict

#Type
Contact = Dict[str, Union[str, bool]]
Contacts = List[Contact]
Favorites = List[Contact]

# Functions
def _change_default(contacts: Contacts, favorites: Favorites, contact_index: int, variable: str):
    variable_change_condition = input(f"Do you wanna change the contact {variable}? (Y/N)")
    if variable_change_condition == "Y" or variable_change_condition == 'y':
        contacts[contact_index][f"{variable.capitalize()}"] = input(f"New contact {variable}: ")
    elif variable_change_condition == "N" or variable_change_condition == 'n':
        contacts[contact_index][f"{variable.capitalize()}"] = contacts[contact_index][f"{variable.capitalize()}"]
    else:
        print("The answer must be Y/y or N/n")
    
    try:
        favorite_index = favorites.index(contacts[contact_index])
        favorites[favorite_index] = contacts[contact_index]
    except:
        pass


def add_contact(contacts: Contacts, contact: Contact) -> None:
    contact = {"Name": contact["Name"], "Phone": contact["Phone"], "Email": contact["Email"], "Favorite": contact["Favorite"]}
    contacts.append(contact)

def see_full_favorite_list(favorites: Favorites) -> None:
    print("\n*******\nFAVORITE LIST:")
    for count, contact in enumerate(favorites, start = 1):
        contact_name = contact["Name"]
        contact_phone = contact["Phone"]
        contact_email = contact["Email"]
        favorite_status = "🌟" if contact["Favorite"] else " "
        print(f"> {count}. [{favorite_status}] {contact_name} | {contact_phone} | {contact_email}")

def see_full_contact_list(contacts: Contacts) -> None:
    print("\n*******\nCONTACT LIST:")
    for count, contact in enumerate(contacts, start = 1):
        contact_name = contact["Name"]
        contact_phone = contact["Phone"]
        contact_email = contact["Email"]
        favorite_status = "🌟" if contact["Favorite"] else " "
        print(f"> {count}. [{favorite_status}] {contact_name} | {contact_phone} | {contact_email}")

def update_contact(contacts: Contacts, favorites: Favorites, contact_index: int) -> None:
    _change_default(contacts, favorites, contact_index, "name")
    _change_default(contacts, favorites, contact_index, "phone")
    _change_default(contacts, favorites, contact_index, "email")
    
def add_to_favorites(contacts: Contacts, contact_index: int, favorites: Favorites) -> None:
    if contacts[contact_index] in favorites:
        print("\nContact already favorited")
        return
    favorites.append(contacts[contact_index])
    contacts[contact_index]["Favorite"] = True

def remove_from_favorites(contacts: Contacts, contact_index: int, favorites: Favorites) -> None:
    if not contacts[contact_index] in favorites:
        print("\nContact is not favorited")
        return
    favorites.remove(contacts[contact_index])
    contacts[contact_index]["Favorite"] = False


# Lists
favorites = []
contacts= []

while True:
    print("""\nTask Manager Menu:
    1. Add contact
    2. See favorite contacts list
    3. See all contacts
    4. Update contact
    5. Add contact to favorites
    6. Remove contact from favorites
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
    elif contact_list_options == "2":
        see_full_favorite_list(favorites)
    elif contact_list_options == "3":
        see_full_contact_list(contacts)
    elif contact_list_options == "4":
        see_full_contact_list(contacts)
        contact_index_to_update = int(input("Select the contact you want to update: ")) - 1
        if contact_index_to_update >= 0 and contact_index_to_update < len(contacts):
            update_contact(contacts, favorites, contact_index_to_update)
            see_full_contact_list(contacts)
        else:
            print("\nContact Invalid") 
        
    elif contact_list_options == "5":
        see_full_contact_list(contacts)
        contact_index_to_favorite = int(input("Select the contact you want to add to Favorite List: ")) - 1
        if contact_index_to_favorite >= 0 and contact_index_to_favorite < len(contacts):
            add_to_favorites(contacts, contact_index_to_favorite, favorites)
            see_full_contact_list(contacts)
        else:
            print("\nContact Invalid")
    elif contact_list_options == "6":
        see_full_contact_list(contacts)
        contact_index_to_favorite = int(input("Select the contact you want to remove from Favorite List: ")) - 1
        if contact_index_to_favorite >= 0 and contact_index_to_favorite < len(contacts):
            remove_from_favorites(contacts, contact_index_to_favorite, favorites)
            see_full_contact_list(contacts)
        else:
            print("\nContact Invalid")
    elif contact_list_options == "7":
        break
    else:
        print("\nOption invalid!")
