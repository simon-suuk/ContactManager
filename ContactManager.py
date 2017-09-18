class Contact:
    def __init__(self, name=None, phone_no="Cylindrical", email=None, gender=None, post_address=None):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.gender = gender
        self.post_address = post_address

    def __repr__(self):
        return self.__dict__

    def get_user_input(self):
        name = input("enter name: ")
        phone_no = input("enter phone_no: ")
        email = input("enter email: ")
        gender = input("enter gender: ")
        post_address = input("enter post_address: ")

        return dict(name=name, phone_no=phone_no, email=email, gender=gender, post_address=post_address)

    def update_contact_details(self, **kwargs):
        self.name = kwargs.get("name")
        self.phone_no = kwargs.get("phone_no")
        self.email = kwargs.get("email")
        self.gender = kwargs.get("gender")
        self.post_address = kwargs.get("post_address")

    def get_contact_details(self, contact_object):
        print("\n***--------------***----------------***")
        print("Name: {name}\nPhone: {phone_no}\nEmail: {email}\nGender: {gender}"
              "\nAddress: {post_address}".format(**contact_object))


# create new contact object
new_contact = Contact()

# get user inputs
update_parameters = new_contact.get_user_input()

# perform update to modify contact details
new_contact.update_contact_details(**update_parameters)

# print contact details
new_contact.get_contact_details(new_contact.__repr__())
