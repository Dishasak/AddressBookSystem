class AddressBookMain:
       
    def create_contact(self):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        address = input("Enter Address: ")
        city = input("Enter City: ")
        state = input("Enter State: ")
        zip1 = input("Enter ZIP Code: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")

        contact = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip1,
            "phone": phone,
            "email": email,
        }
address_book = AddressBookMain()
address_book.create_contact()