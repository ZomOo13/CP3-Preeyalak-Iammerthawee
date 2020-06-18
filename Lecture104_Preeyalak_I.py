class Customer :
    name = ""
    lastname = ""
    phone = ""

    def data(self):
        print("Name :",self.name,self.lastname)
        print("Phone :",self.phone)

customer1 = Customer()
customer1.name = "Zom"
customer1.lastname = "Iam"
customer1.phone = "0888888888"
customer1.data()

customer2 = Customer()
customer2.name = "Minie"
customer2.lastname = "Mei"
customer2.phone = "0987654321"
customer2.data()

customer3 = Customer()
customer3.name = "Foxxy"
customer3.lastname = "Nane"
customer3.phone = "0112223333"
customer3.data()

customer4 = Customer()
customer4.name = "Rosie"
customer4.lastname = "Mei"
customer4.phone = "0123456789"
customer4.data()