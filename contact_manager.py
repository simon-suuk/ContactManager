import csv
import os


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

    def set_name(self, name):
        self.name = name

    def set_phone_no(self, phone_no):
        self.phone_no = phone_no

    def set_email(self, email):
        self.email = email

    def set_gender(self, gender):
        self.gender = gender

    def set_post_address(self, post_address):
        self.post_address = post_address

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
        remove_result = None
        with open(self.contacts_file, 'r', newline="") as source_file, \
                open("temp_file.csv", "a", newline="") as destination_file:
            temp_file_writer = csv.writer(destination_file)
            for row in csv.reader(source_file):
                if name not in row:
                    temp_file_writer.writerow(row)
                else:
                    remove_result = row[0], row[1], row[2], row[3], row[4]
        os.remove(self.contacts_file)
        os.renames("temp_file.csv", self.contacts_file)
        return remove_result

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
          "\n 3. \"r\" to remove contact"
          "\n 4. \"e\" to edit contact\n")

    # get command issued by user
    command = input("command? ---> ")

    contact_list = ContactManager("contact_list.csv")

    while command != "q":
        if command == "a":
            # get user inputs returned as a dictionary
            # unpack the values to respective instance variables
            c_name, c_phone_no, c_email, c_gender, c_post_address = capture_input().values()

            # create new contact object with user inputs
            new_contact = Contact(c_name, c_phone_no, c_email, c_gender, c_post_address)

            # add contact to list
            contact_list.add_contact(new_contact)
        elif command == "s":
            contact_name = input("contact name? ---> ")
            # search for contact by name
            search_results = contact_list.search_contact(contact_name)
            if search_results is not None:
                r_name, r_phone_no, r_email, r_gender, r_post_address = search_results
                show_contact_details(r_name, r_phone_no, r_email, r_gender, r_post_address)
            else:
                print("search result: {}".format(search_results))
                print("")
        elif command == "r":
            contact_name = input("contact name? ---> ")
            # delete a contact by name
            remove_results = contact_list.remove_contact(contact_name)
            if remove_results is not None:
                r_name, r_phone_no, r_email, r_gender, r_post_address = remove_results
                show_contact_details(r_name, r_phone_no, r_email, r_gender, r_post_address)
            else:
                print("remove result: {}".format(remove_results))
                print("")
        elif command == "e":
            pass
            # perform update to modify contact details
            # update_details = capture_input()
            # new_contact.update_contact_details(**update_details)
        else:
            print("Sorry, I don't understand you")

        # get command issued by user
        command = input("command? ---> ")
        print("")
