'''การใช้งานเงื่อนไขซ้อนเงื่อนไข (Nested Condition)'''

print("        LOGIN        ")
print("---------------------")
usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "zomzom" and passwordInput == "1111":
   product1 = "candy" or "3"
   product2 = "beer" or "4"
   price1 = int(5)
   price2 = int(65)
   print("WELCOME TO 109 SHOP")
   print(" Product list  ")
   print("1.",product1,":   ",price1,"฿")
   print("2.",product2,":   ",price2,"฿")
   userSelected1 = input("Select product number :")
   piece1 = int(input("piece :"))
   done1 = input("Other products (yes/no) : ")
   if done1 == "yes" :
       userSelected2 = input("Select product :")
       piece2 = int(input("piece :"))
       print("    Your Order    ")
       if userSelected1 == "1" and userSelected2 == "2" :
           print("1.", product1, "x", piece1, ":", price1 * piece1, "฿")
           print("2.", product2, "x", piece2, ":", price2 * piece2, "฿")
           print("---------------------")
           print("Total", (price1 * piece1) + (price2 * piece2), "฿")
       elif userSelected1 == "2" and userSelected2 == "1" :
           print("1.", product2, "x", piece1, ":", price2 * piece1, "฿")
           print("2.", product1, "x", piece2, ":", price1 * piece2, "฿")
           print("---------------------")
           print("Total",(price2 * piece1)+(price1 * piece2),"฿" )
   elif done1 == "no" :
       print("    Your Order    ")
       if userSelected1 == "1" :
           print("1.",product1,"x",piece1,":",price1*piece1,"฿")
           print("---------------------")
           print("Total",price1*piece1,"฿" )
       elif userSelected1 == "2" :
           print("1.",product2,"x",piece1,":",price2*piece1,"฿")
           print("---------------------")
           print("Total",price2*piece1,"฿")
   else:
       print("ERROR !!!")
else:
    print("ERROR !!!")
print("---------------------")
print("------THANK TOU------")