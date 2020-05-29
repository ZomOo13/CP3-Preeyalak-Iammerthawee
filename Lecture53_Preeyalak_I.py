Price = float(input("Total Price = "))
def vatCal(Price) :
    result = Price+(Price*7/100)
    return result
print(vatCal(Price))