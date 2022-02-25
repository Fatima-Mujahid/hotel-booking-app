import re
import datetime
import os


# -----Hotel booking class-----

class HotelBookingApp:

    # -----Default constructor-----

    def __init__(self):
        self.num_of_days = 0
        self.amount = 0
        self.allotment = ""
        self.name = ""
        self.birthday = ""
        self.cnic = ""
        self.cnic_photocopy = ""
        self.rating = 0

    # -----Input and validate number of days-----  

    def get_num_of_days(self):
        while True:
            try:

                num_of_days = int(input("\nEnter number of days (1 to 7): "))

                if 1 <= num_of_days <= 7:
                    self.num_of_days = num_of_days
                    break
                else:
                    print("INVALID INPUT!\nRoom can only be booked for a period of 1 to 7 days.")

            except ValueError:
                print("INVALID INPUT!\nNumber of days must be a valid integer.")
                pass

        return self.num_of_days

    # -----Input and validate amount to pay per day-----

    def get_amount(self):
        while True:
            try:
                print(
                    "\nLess than 10000 -> Studio\n10000 to 25000 -> Executive Suite\nGreater than 50000 -> "
                    "Cabana\n25001 to 49999 -> No rooms available")
                amount = int(input("\nEnter amount to pay per day: "))

                valid = True
                if amount < 0:
                    print("INVALID INPUT!\nRAmount cannot be negative.")
                    valid = False
                    pass
                elif amount < 10000:
                    print("You are allotted a Studio.")
                    self.allotment = "Studio"
                    break
                elif amount <= 25000:
                    print("You are allotted an Executive Suite.")
                    self.allotment = "Executive Suite"
                    break
                elif amount < 50000:
                    print("INVALID INPUT!\nHotel does not provide rooms between Rs. 25001 to 49999.")
                    valid = False
                    pass
                else:
                    print("You are allotted a Cabana.")
                    self.allotment = "Cabana"
                    break

                if valid: self.amount = amount

            except ValueError:
                print("INVALID INPUT!\nAmount must be a valid integer.")
                pass
        return self.allotment

    # -----Input user name-----

    def get_user_name(self):
        while True:
            # Input name
            name = input("\nEnter name: ")
            pattern = re.compile("^[a-zA-Z ]+$")
            if (pattern.match(name) and name.istitle()):
                self.name = name
                break
            else:
                print("INVALID INPUT!\nName must be alphabetic and in title case.")
                pass
        return self.name

    # -----Input user birthday-----

    def get_user_birthday(self):
        while True:
            try:
                # Input birthday
                birthday = input("\nEnter birthday (dd-mm-yyyy): ")
                datetime.datetime.strptime(birthday, "%d-%m-%Y")
                self.birthday = birthday
                break
            except ValueError:
                print("INVALID INPUT!\nDate should be valid and in format dd-mm-yyyy.")
                pass
        return self.birthday

    # -----Input user cnic number-----

    def get_user_cnic(self):
        while True:
            # Input cnic number
            cnic = input("\nEnter CNIC number: ")

            if len(cnic) == 13 and re.match('^[0-9]*$', cnic):
                self.cnic = cnic
                break
            else:
                print("INVALID INPUT!\nCNIC number must be numeric and exactly 13 digits.")
                pass
        return self.cnic

    # -----Input cnic photocopy path-----

    def get_cnic_photocopy(self):
        while True:
            cnic_photocopy = input("\nEnter absolute path of cnic photocopy: ")

            if os.path.isfile(cnic_photocopy):
                if cnic_photocopy.endswith((".jpg", ".png")):
                    self.cnic_photocopy = cnic_photocopy
                    break
                else:
                    print("INVALID INPUT!\nFile format must be .jpeg or .png.")
                    pass
            else:
                print("INVALID PATH!\nFile does not exist.")
                pass
        return self.cnic_photocopy

    # -----Input and validate rating-----

    def get_rating(self):
        while True:
            try:
                rating = int(input("\nRate your experience (1 to 5) or Enter 0 to skip rating: "))
                print(rating)
                if rating != 0 and (rating < 1 or rating > 5):
                    print("INVALID INPUT!\nRating can only be 1, 2, 3, 4 or 5. Enter 0 to skip rating")
                    pass
                else:
                    self.rating = rating
                    break

            except ValueError:
                print("INVALID INPUT!\nRating must be a valid integer.")
                pass

        return self.rating

    # -----Output booking details-----

    def display(self):
        print("\n----------BOOKING DETAILS----------\n")
        print("Number of days: ", self.num_of_days)
        print("Amount per day: Rs. ", self.amount)
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("CNIC number: ", self.cnic)
        print("CNIC photocopy path: ", self.cnic_photocopy)
        print("Rating: ", "Not rated yet" if self.rating == 0 else self.rating, "\n")


# -----Driver code-----
# Object instantiation

h1 = HotelBookingApp()

# Accessing class methods

# print("\n----------HOTEL BOOKING APP----------")
# h1.get_num_of_days()
# h1.get_amount()
# h1.get_user_name()
# h1.get_user_birthday()
# h1.get_user_cnic()
# h1.get_cnic_photocopy()
# h1.get_rating()
# h1.display()
