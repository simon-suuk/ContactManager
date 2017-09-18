class Contact:
    def __init__(self, name=None, phone_no="Cylindrical", email=None, gender=None, post_address=None):
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.gender = gender
        self.post_address = post_address

    def get_user_input(self):
        name = input("enter name: ")
        phone_no = input("enter phone_no: ")
        email = input("enter email: ")
        gender = input("enter gender: ")
        post_address = input("enter post_address: ")

        return dict(name=name, phone_no=phone_no, email=email, gender=gender, post_address=post_address)