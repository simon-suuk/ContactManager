import csv


def capture_input():
    nm = input("enter name: ")
    ph = input("enter phone number: ")
    em = input("enter email: ")
    g = input("enter gender: ")
    p_adr = input("enter post_address: ")
    return dict(name=nm, phone_no=ph, email=em,
                gender=g, post_address=p_adr)


def show_contact_details(name, phone_no, email, gender, post_address):
    print("\n***--------------***----------------***")
    print("Name: {}"
          "\nPhone: {}"
          "\nEmail: {}"
          "\nGender: {}"
          "\nAddress: {}".format(name, phone_no, email, gender, post_address))
    print("***--------------***----------------***")


class Contact:
    def __init__(self, name=None, phone_no=0,
                 email=None, gender=None, post_address=None):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.gender = gender
        self.post_address = post_address

    def __repr__(self):
        return self.__dict__

    def get_name(self):
        return self.name

    def get_phone_no(self):
        return self.phone_no

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def get_post_address(self):
        return self.post_address

    def update_contact_details(self, **kwargs):
        self.name = kwargs.get("name")
        self.phone_no = kwargs.get("phone_no")
        self.email = kwargs.get("email")
        self.gender = kwargs.get("gender")
        self.post_address = kwargs.get("post_address")


class ContactManager:
    def __init__(self, contacts_file=""):
        if contacts_file == "":
            self.contacts_file = "temp_file.csv"
        else:
            self.contacts_file = contacts_file

    def add_contact(self, contact):
        with open(self.contacts_file, 'a', newline="") as file_to_append_to:
            add_contact_file_writer = csv.writer(file_to_append_to)
            add_contact_file_writer.writerow([contact.get_name(), contact.get_phone_no(),
                                             contact.get_email(), contact.get_gender(),
                                             contact.get_post_address()])

    def remove_contact(self, name):
        with open(self.contacts_file, 'r', newline="") as file_to_search:
            search_contact_file_reader = csv.reader(file_to_search)
            for row in search_contact_file_reader:
                if name in row:
                    return row[0], row[1], row[2], row[3], row[4]
        return None

    def search_contact(self, name):
        with open(self.contacts_file, 'r', newline="") as file_to_search:
            search_contact_file_reader = csv.reader(file_to_search)
            for row in search_contact_file_reader:
                if name in row:
                    return row[0], row[1], row[2], row[3], row[4]
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

    contact_list = ContactManager("contact_list.csv")

    contact_list.add_contact(new_contact)

    search_results = contact_list.search_contact("simon")
    if search_results is not None:
        r_name, r_phone_no, r_email, r_gender, r_post_address = search_results
        show_contact_details(r_name, r_phone_no, r_email, r_gender, r_post_address)
    else:
        print("search result: {}".format(search_results))
