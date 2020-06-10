systemMenu = {"มังคุด": 25, "เงาะ": 35, "ทุเรียน": 120, "ส้ม": 45}
menuList = []

while True:
    menu = input('Please Enter Menu : ').lower()
    if menu == 'exit':
        break
    else:
        menuList.append([menu,systemMenu[menu]])

def showBill() :
    total = 0
    print('Your Food'.center(21,'*'))
    for food in range(len(menuList)):
        print(menuList[food][0],menuList[food][1])
        total += menuList[food][1]
    print('total :', total)

showBill()
