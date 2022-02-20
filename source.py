import re
import datetime
import os

# -----Hotel booking class-----

class HotelBookingApp:

    # -----Default constructor-----

    def __init__(self):
        self.num_of_days = 0
        self.amount = 0
        self.name = ""
        self.birthday = ""
        self.cnic = ""
        self.cnic_photocopy = "" 
        self.rating = 0

    # -----Input and validate number of days-----  

    def get_num_of_days(self):
        self.num_of_days = input("\nEnter number of days (1 to 7): ")

        try: 
            self.num_of_days = int(self.num_of_days)
            if (self.num_of_days < 1 or self.num_of_days > 7):
                print("INVALID INPUT!\nRoom can only be booked for a period of 1 to 7 days.")

        except ValueError: 
            print("INVALID INPUT!\nNumber of days must be a valid integer.")

    # -----Input and validate amount to pay per day-----

    def get_amount(self):
        self.amount = input("\nEnter amount to pay per day: ")

        try: 
            self.amount = int(self.amount)
            if (self.amount < 0):
                print("INVALID INPUT!\nRAmount cannot be negative.")
            elif (self.amount < 10000):
                print("You are allotted a Studio.")
            elif (self.amount <= 25000):
                print("You are allotted an Executive Suite.")
            elif (self.amount < 50000):
                print("INVALID INPUT!\nHotel does not provide rooms between Rs. 25001 to 49999.")
            else:
                print("You are allotted a Cabana.")

        except ValueError: 
            print("INVALID INPUT!\nAmount must be a valid integer.")

    # -----Input and validate user info (name, birthday and cnic number)-----

    def get_user_info(self):

        # Input name
        self.name = input("\nEnter name: ")
        pattern = re.compile("^[a-zA-Z ]+$")

        if (not(pattern.match(self.name) and self.name.istitle())):
            print("INVALID INPUT!\nName must be alphabetic and in title case.")

        # Input birthday
        self.birthday = input("\nEnter birthday (dd-mm-yyyy): ")

        try:
            datetime.datetime.strptime(self.birthday, "%d-%m-%Y")

        except ValueError:
            print("INVALID INPUT!\nDate should be valid and in format dd-mm-yyyy.")

        # Input cnic number
        self.cnic = input("\nEnter CNIC number: ")

        if (not(len(self.cnic) == 13 and re.match('^[0-9]*$', self.cnic))):
            print("INVALID INPUT!\nCNIC number must be numeric and exactly 13 digits.")

    # -----Input cnic photocopy path-----

    def get_cnic_photocopy(self):
        self.cnic_photocopy = input("\nEnter absolute path of cnic photocopy: ")

        if (os.path.isfile(self.cnic_photocopy)):
            if (not(self.cnic_photocopy.endswith((".jpeg", ".png")))):
                print ("INVALID INPUT!\nFile format must be .jpeg or .png.")
        
        else:
            print ("INVALID PATH!\nFile does not exist.")

    # -----Input and validate rating-----

    def get_rating(self):
        self.rating = input("\nRate your experience (1 to 5) or Enter 0 to skip rating: ")
        
        try: 
            self.rating = int(self.rating)
            if (self.rating != 0 and (self.rating < 1 or self.rating > 5)):
                print("INVALID INPUT!\nRating can only be 1, 2, 3, 4 or 5.")

        except ValueError: 
            print("INVALID INPUT!\nRating must be a valid integer.")

    # -----Output booking details-----

    def display(self):
        print("\n----------BOOKING DETAILS----------\n")
        print("Number of days: ", self.num_of_days)
        print("Amount per day: ", self.amount)
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("CNIC number: ", self.cnic)
        print("CNIC photocopy path: ", self.cnic_photocopy)
        print("Rating: ", "Not rated yet" if self.rating == 0 else self.rating, "\n")
  
# -----Driver code-----
# Object instantiation

h1 = HotelBookingApp()
  
# Accessing class methods

print("\n----------HOTEL BOOKING APP----------")
h1.get_num_of_days()
h1.get_amount()
h1.get_user_info()
h1.get_cnic_photocopy()
h1.get_rating()
h1.display()