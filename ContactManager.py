def capture_input():
    nm = input("enter name: ")
    ph = input("enter phone number: ")
    em = input("enter email: ")
    g = input("enter gender: ")
    p_adr = input("enter post_address: ")
    return dict(name=nm, phone_no=ph, email=em,
                gender=g, post_address=p_adr)


class Contact:
    def __init__(self, name=None, phone_no="Cylindrical",
                 email=None, gender=None, post_address=None):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.gender = gender
        self.post_address = post_address

    def __repr__(self):
        return self.__dict__

    def update_contact_details(self, **kwargs):
        self.name = kwargs.get("name")
        self.phone_no = kwargs.get("phone_no")
        self.email = kwargs.get("email")
        self.gender = kwargs.get("gender")
        self.post_address = kwargs.get("post_address")

    def show_contact_details(self):
        print("\n***--------------***----------------***")
        print("Name: {name}"
              "\nPhone: {phone_no}"
              "\nEmail: {email}"
              "\nGender: {gender}"
              "\nAddress: {post_address}".format(**self.__repr__()))
        print("***--------------***----------------***")


class ContactManager:
    def __init__(self, contacts=[]):
        self.contacts = contacts

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return contact
        return None

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

if __name__ == "__main__":
    print("Welcome to ContactManager!"
          "\nYou can use the following commands:"
          "\n 1. \"a\" to add new contact"
          "\n 2. \"s\" to search contact"
          "\n 3. \"r\" to remove contact\n")

    # get command issued by user
    command = input()

    # get user inputs returned as a dictionary
    # unpack the values to respective instance variables
    c_name, c_phone_no, c_email, c_gender, c_post_address = capture_input().values()

    # create new contact object with user inputs
    new_contact = Contact(c_name, c_phone_no, c_email, c_gender, c_post_address)

    # perform update to modify contact details
    # update_details = capture_input()
    # new_contact.update_contact_details(**update_details)

    # print contact details
    # new_contact.show_contact_details()

    contact_list = ContactManager()

    contact_list.add_contact(new_contact)

    search_results = contact_list.search_contact("simon")
    if search_results is not None:
        search_results.show_contact_details()
    else:
        print("search result: {}".format(search_results))
