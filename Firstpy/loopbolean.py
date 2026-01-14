print("Hello world!")

dayow = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

while True:
    day = str(input("Choose a day of the week!\n")).strip().title()#not case sensitive
    if day in dayow:
        print(f"You choose {day}!")
        tryagain = str(input("Try again? [Y/N]\n")).strip().upper() # y,n -> Y,N
        if tryagain !="Y":
            print("Goodbye");
            break
    else:
        print("Invalid day, Try again!");
        


    
    
