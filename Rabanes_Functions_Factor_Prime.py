import time

def Loading():
    animation = ['Loading.', 'Loading..', 'Loading...', 'Loading....']
    for i in range(5):
        for frame in animation:
            print(frame, end='\r')
            time.sleep(0.2)
    print("Program successfully loaded."
          "\n")

def sff():
    print('Program "Smallest Factor Finder (SFF)" is initiating')
    Loading()
    while True:
        n = int(input("Enter Integer >=2: "))
        if n >= 2:
            factor = 0
            
            for i in range(2, n+1):
                if n % i == 0:
                    factor = i
                    print(f"The Smallest factor of {n} other than 1 is {factor}")
                    break
                
            choice = input("Continue? [Y/N]: ")
            while choice.lower() not in ['y', 'n']:
                print("Invalid Input. Enter Y or N only")
                choice = input("Continue? [Y/N]: ")
            
            if choice.lower() == 'n':
                print("Thank you for using SFF <3")
                break
        else:
            print("Invalid Number. Enter a number greater than 2.")

def prime():
    print('Program "Prime numbers within a range" is initiating')
    Loading()
    while True:
        start = float(input("Enter a number [start]: "))
        check1 = True
        if start < 0:
            print("Enter a non-negative number.")
            check1 = False
            continue
        elif start == 0:
            print("Program Terminated.")
            check1 = False
            break
        elif not start.is_integer():
            print("Enter an integer number only.")
            check1 = False
            continue

        while True:
            end = float(input("Enter a number [end]: "))
            check2 = True
            if end < 0:
                print("Enter a non-negative number.")
                check2 = False
                continue
            elif end == 0:
                print("Program Terminated.")
                check2 = False
                break
            elif end <= start:
                print(f"Enter a number greater than {int(start)}."
                    "\n")
                check2 = False
                continue
            elif not end.is_integer():
                print("Enter an integer number only.")
                check2 = False
                continue
            
            start = int(start)
            end = int(end)
            result = ""
            if start <= 2 <= end: #include 2 if its in the range
                result += "2 " # since 2 % 2 = 0 therefore the code will make 2 as not a prime number.
            if start == 1: 
                for i in range(2, end): # 1 is a special number so we skip it
                    if i % 2 != 0: # checks if the number is uneven. p.s not all uneven numbers are prime but prime numbers except for 2 are uneven.
                        result += str(i) + " "
            else:
                for i in range(start, end): 
                    if i % 2 != 0:
                        result += str(i) + " "

            if check1 and check2 == True:
                print(f"The Prime numbers between {start} and {end} is {result}" # following the screenshot
                    '\n')
                break
        if end == 0:
            break

def step1():
    print("CS112: COMPUTER PROGRAMMING 1 - SFF & PRIME NUMBERS"
      "\nCreated by: Francis Alfred R. Rabanes"
      "\n"
      "\nProblem: Create python program that displays all prime numbers within a range or to find the smallest factor of a number:"
      "\n"
      "\nRULES:"
      "\n[1] FOR PRIME NUMBERS WITHIN A RANGE "
      '\n[-] If number (start) is a negative number. The program will prompt a message “Enter a non-negative number.”'
      '\n[-] If number (end) is less than number (start). The program will prompt a message “Enter a number greater than number (start).”'
      '\n[-] Lastly, if the user enter the number “0”, the program will terminate.'
      "\n"
      "\n[2] FOR SMALLEST FACTOR FINDER ( SFF )"
      "\n[-] Enter numbers that are only greater than 2."
      "\n"
      )

    while True:
        print("\nCHOICES:"
              "\n[1] Prime Numbers within a range."
              "\n[2] Smalles Factor Finder (SFF)."
              "\n[3] End The Program.")
        choice = int(input("Enter what type of program to use [1] or [2]: "))
        print("\n")
        if choice == 1:
            prime()

        elif choice == 2:
            sff()

        elif choice == 3:
            print("Program Terminated.")
            break
        else:
            print("Invalid input. Enter number 1 or 2 only,")
            continue


step1()
