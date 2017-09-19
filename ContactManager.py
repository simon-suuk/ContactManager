def capture_input():
    name = input("enter name: ")
    phone_no = input("enter phone_no: ")
    email = input("enter email: ")
    gender = input("enter gender: ")
    post_address = input("enter post_address: ")
    return dict(name=name, phone_no=phone_no, email=email,
                gender=gender, post_address=post_address)


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


# get user inputs
contact_details = capture_input()

# create new contact object
new_contact = Contact()

# perform update to modify contact details
new_contact.update_contact(**contact_details)

# print contact details
new_contact.show_contact()
