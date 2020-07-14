menuList = []
priceList = []

while True:
    menu = input('Please Enter Menu : ').lower()
    if menu == 'exit':
        break
    else:
        price = int(input('Price : '))
        menuList.append(menu)
        priceList.append(price)

def showBill() :
    total = 0
    print('Your Food'.center(21,'*'))
    for food in range(len(menuList)):
        print(menuList[food],priceList[food])
        total += priceList[food]
    print('total :', total)

showBill()