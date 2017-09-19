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


if __name__ == "__main__":
    # get user inputs returned as a dictionary
    # unpack the values to respective instance variables
    name, phone_no, email, gender, post_address = capture_input().values()

    # create new contact object with user inputs
    new_contact = Contact(name, phone_no, email, gender, post_address)

    # perform update to modify contact details
    # update_details = capture_input()
    # new_contact.update_contact(**update_details)

    # print contact details
    new_contact.show_contact()
