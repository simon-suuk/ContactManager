def capture_input():
    nm = input("enter nm: ")
    ph = input("enter phone: ")
    em = input("enter em: ")
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

    def update_contact(self, **kwargs):
        self.name = kwargs.get("name")
        self.phone_no = kwargs.get("phone_no")
        self.email = kwargs.get("email")
        self.gender = kwargs.get("gender")
        self.post_address = kwargs.get("post_address")

    def show_contact(self):
        print("\n***--------------***----------------***")
        print("Name: {name}"
              "\nPhone: {phone_no}"
              "\nEmail: {email}"
              "\nGender: {gender}"
              "\nAddress: {post_address}".format(**self.__repr__()))


class ContactManager:
    def __init__(self, contacts=[]):
        self.markers = contacts

    def add_contact(self, contact):
        self.markers.append(contact)


if __name__ == "__main__":
    # get user inputs returned as a dictionary
    # unpack the values to respective instance variables
    c_name, c_phone_no, c_email, c_gender, c_post_address = capture_input().values()

    # create new contact object with user inputs
    new_contact = Contact(c_name, c_phone_no, c_email, c_gender, c_post_address)

    # perform update to modify contact details
    # update_details = capture_input()
    # new_contact.update_contact(**update_details)

    # print contact details
    new_contact.show_contact()
