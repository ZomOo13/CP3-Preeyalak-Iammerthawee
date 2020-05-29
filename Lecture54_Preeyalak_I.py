def login() :
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "zomzom" and passwordInput == "1111":
        return showMenu()
    else:
        return login()
def showMenu() :
    print("----*---- zShop ----*----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    select()
def select() :
    Select = int(input("Select >> "))
    if Select == 1:
        return vatCal(int(input("totalprice >> ")))
    elif Select == 2:
        return priceCal()
def vatCal(totalprice) :
    vat = int(input("vat(%) >> "))
    result = totalprice+(totalprice*vat/100)
    return print(result)
def priceCal() :
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCal(price1+price2)

print("---*---*---LOGIN---*---*--")
login()
print("---*---* THANK YOU *---*--")


