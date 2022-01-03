#Function
def menu ():
    print("---Choose the menu---")
    print("1. Espresso")
    print("2. Cappucino")
    print("3. Latte")
    
def HotorCold():
    print("---Choose the type of the coffee---")
    print("1. Hot")
    print("2. Cold ")

def space():
    print("")

def size():
    print("---Size of Cup---")
    print("1. Small for 20 bath")
    print("2. medium for 30 bath")
    print("3. Big for 40 bath")

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
Type_Cup = ""
sm = "small"
m = "medium"
b = "big"

#code

print("---Welcome to Nut's Coffee---")
space()

select_type = (int(input("please type 1 to show our menu : ")))
space()
if select_type == 1:
    menu()
    select_menu = int(input("Select coffee: "))
    space()
    if select_menu >0 and select_menu <=3:
        if select_menu == 1:
            Type_Menu += es
        elif select_menu == 2:
            Type_Menu  += cp
        elif select_menu == 3:
            Type_Menu  += lt
    else:
        space()
        print("---Type 1 or 2 or 3 only please try again---")
    
    if es in Type_Menu or cp in Type_Menu or lt in Type_Menu:
        HotorCold()
        select_HC = int(input("Select type:"))
        space()
        if select_HC >=0 and select_HC <=2:
            size()
            size_c = int(input("What Size did you want: "))
            if size_c == 1:
                Type_Cup += sm
            elif size_c == 2:
                Type_Cup += m 
            elif size_c == 3:
                Type_Cup += b
            else:
                space()
                print("---Type 1 or 2 or 3 please try again---")
        else:
            space()
            print("------Type 1 or 2 only please try again------")
            
        if select_HC>0 and select_HC <=2 :
            if select_HC == 1 and size_c == 1:
                Type_HC += h
                space()
                print("---You choose %s hot %s 20 bath---"%(Type_Cup,Type_Menu))
            elif select_HC == 1 and size_c == 2:
                Type_HC += c 
                space() 
                print("---You choose %s cold %s 30 bath---"%(Type_Cup,Type_Menu))
                
            elif select_HC == 1 and size_c == 3:
                Type_HC += c  
                space()
                print("---You choose %s cold %s 40 bath---"%(Type_Cup,Type_Menu))
                
            elif select_HC == 2 and size_c == 1:
                Type_HC += c  
                space() 
                print("---You choose %s cold %s 20 bath---"%(Type_Cup,Type_Menu))
                
            elif select_HC == 2 and size_c == 2:
                Type_HC += c  
                space()
                print("---You choose %s cold %s 30 bath---"%(Type_Cup,Type_Menu))
                 
            elif select_HC == 2 and size_c ==3:
                Type_HC += c  
                space()
                print("---You choose %s cold %s 40 bath---"%(Type_Cup,Type_Menu))
                                     
    
        
    if "hot" in Type_HC or "cold" in Type_HC :
        money = int(input("Input your money: "))
        if money == 20 or money == 30 or money == 40:
            if money == 20 and Type_HC == h and Type_Cup == sm:
                space()
                print("---Please wait---")
                print("---Thank you---")
                print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
            
                    
            elif money == 30 and Type_HC == h and Type_Cup == m:
                space()
                print("---Please wait---")
                print("---Thank you---")
                print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
                                   
                    
            elif money ==40 and Type_HC == h and Type_Cup == b:
                space()
                print("---Please wait---")
                print("---Thank you---")
                print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
            
            elif money == 20 and Type_HC == c and Type_Cup == sm:
                space()
                print("---Please wait---")
                print("---Thank you---")
                print("---our %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
            
                    
            elif money == 30 and Type_HC == c and Type_Cup == m:
                space()
                print("---Please wait---")
                print("---Thank you---")
                print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
                                   
                    
            elif money ==40 and Type_HC == c and Type_Cup == b:
                space()
                print("---Please wait---")
                print("---Thank you---")
                print("---Your %s %s %s is here enjoy with us coffee---"%(Type_Cup,Type_HC,Type_Menu))
            
            else:
                space()
                print("---Your money isn't true with this order please contact the Owner ---")                                    
        else: 
            space()
            print("---Please Insert your money follow the order please contact the Owner ---")

else: 
    space()
    print("---Type 1 only please try again---")

