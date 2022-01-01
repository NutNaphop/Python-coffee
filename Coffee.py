#Function
def menu ():
    print("---Choose the menu---")
    print("1. Espresso")
    print("2. Cappucino")
    print("3. Latte")
    
def HotorCold():
    print("---Choose the type of the coffee---")
    print("1. Hot 55 Bath")
    print("2. Cold 60 Bath")

def space():
    print("")

#Global Var
Hot = 55
Cold = 60
es = "Espresso"
cp = "Cappucino"
lt = "Latte"
h = "hot"
c = "cold"
Type_Menu = ""
Type_HC = ""

#code
print("---Welcome to Nut's Coffee---")
space()

select_type = (int(input("please type 1 to show menu : ")))

space()
if select_type == 1:
    menu()
    space()
    select_menu = int(input("Select coffee: "))
    if select_menu >0 and select_menu <=3:
        if select_menu == 1:
            Type_Menu += es
        elif select_menu == 2:
            Type_Menu  += cp
        elif select_menu == 3:
            Type_Menu  += lt
    else:
        space()
        print("---Something Went Wrong Pls Try again---")
    
    if es in Type_Menu or cp in Type_Menu or lt in Type_Menu:
        HotorCold()
        space()
        select_HC = int(input("Select type:"))
        if select_HC>0 and select_HC <=2:
            if select_HC == 1:
                Type_HC += h
                print("---You chose hot %s 55 bath---"%Type_Menu)
                space()
            elif select_HC == 2:
                Type_HC += c  
                print("---You choose cold %s 60 bath---"%Type_Menu)
                space()
        else:
            space()
            print("---Something Went Wrong Pls Try again---")
    
    if "hot" in Type_HC or "cold" in Type_HC:
        money = int(input("Input your money:"))
        if money >=55 and Type_HC == h :
            if money>=55:
                pay = money-55
                print("You recieved a change of %d Bath"%pay)
                print("---Thank you---")             
        if money >=60 and Type_HC == c:
            if money>=60:
                pay = money-60
                print("You recieved a change of %d Bath"%pay)
                print("---Thank you---")
        elif money < 60:
            print("---Something Went Wrong Pls Try again---")
            

else: 
    print("---Something Went Wrong Pls Try again---")


