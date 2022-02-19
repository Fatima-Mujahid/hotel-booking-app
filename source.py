class HotelBookingApp:

    # Default constructor
    def __init__(self):
        self.num_of_days = 0
        self.amount = 0
        self.name = ""
        self.birthday = ""
        self.cnic = ""
        self.cnic_photocopy = "" 
        self.rating = 0
          
    def get_num_of_days(self):
        self.num_of_days = input("Enter number of days (1 to 7): ")
        try: 
            self.num_of_days = int(self.num_of_days)
            if (self.num_of_days < 1 or self.num_of_days > 7):
                print("INVALID INPUT!\nRoom can only be booked for a period of 1 to 7 days.")

        except ValueError: 
            print("INVALID INPUT!\nNumber of days should be a valid integer.")
    
    def get_amount(self):
        self.amount = input("Enter amount to pay per day: ")
        try: 
            self.amount = int(self.amount)
            if (self.amount < 0):
                print("INVALID INPUT!\nRAmount cannot be negative.")
            elif (self.amount < 10000):
                print("You are allotted a Studio.")
            elif (self.amount <= 25000):
                print("You are allotted an Executive Suite.")
            elif (self.amount < 50000):
                print("Hotel does not provide rooms between Rs. 25001 to 49999.")
            else:
                print("You are allotted a Cabana.")

        except ValueError: 
            print("INVALID INPUT!\nAmount should be a valid integer.")

    def get_user_info(self):
        self.name = input("Enter name: ")
        self.birthday = input("Enter birthday: ")
        self.cnic = input("Enter cnic number: ")

    def get_cnic_photocopy(self):
        self.cnic_photocopy = input("Enter absolute path of cnic photocopy: ")

    def get_rating(self):
        self.rating = int(input("Enter rating: "))

    def display(self):
        print("\n----------INFO----------\n")
        print("Number of days: ", self.num_of_days)
        print("Amount: ", self.amount)
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("CNIC number: ", self.cnic)
        print("CNIC photocopy path: ", self.cnic_photocopy)
        print("Rating: ", self.rating)
  
# Driver code
# Object instantiation
h1 = HotelBookingApp()
  
# Accessing class methods
h1.get_num_of_days()
h1.get_amount()
h1.get_user_info()
h1.get_cnic_photocopy()
h1.get_rating()
h1.display()