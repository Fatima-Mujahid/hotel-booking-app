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
        self.num_of_days = int(input("Enter number of days: "))
    
    def get_amount(self):
        self.amount = int(input("Enter amount: "))

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