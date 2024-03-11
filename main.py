def Programm ():
    while True:
        try:
            Grade = int(input("Enter your mark : "))
            if Grade >= 0 and Grade <= 100:
                break
            else:
                print("Error :( !! Please choose a mark from 0 to 100")
        except:
            print("Error :( !! Please choose a mark from 0 to 100")
    if Grade >= 90 :
        print("Your grade is : A+")
    elif Grade >= 85 and Grade < 90 :
        print("Your grade is : A")
    elif Grade >= 80 and Grade < 85 :
        print("Your grade is : B+")
    elif Grade >= 75 and Grade < 80 :
        print("Your grade is : B")
    elif Grade >= 70 and Grade < 75 :
        print("Your grade is : C+")
    elif Grade >= 65 and Grade < 70 :
        print("Your grade is : C")
    elif Grade >= 60 and Grade < 65 :
        print("Your grade is : D+")
    elif Grade >= 50 and Grade < 60 :
        print("Your grade is : D")
    else:
        print("Your grade is : F")
        
Programm()
A = "Yes repeat Programm"
B = "Exit Programm"        

while True:
    while True:
        try:
            Answer = str(input("Do you want to repeat this Programm and Calculate another mark?\nTo repeat Programm choose : A \nTo Exit Programm choose : B \nPlease choose 'A' or 'B' : "))
            if Answer == 'A' or Answer == 'B':
                break
            else:
                print("Error :( !! Please choose 'A' or 'B'")
        except:
            print("Error :( !! Please choose 'A' or 'B'")
    if Answer == 'A':
        Programm()
    if Answer == 'B':
        print("Good Bye :) !!")
        break

    

