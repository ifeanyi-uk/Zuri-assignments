#register
# - first name, last name, password, email
# - generaten user account


#login
# - account number & password


#bank operations

#Initializing the system
import random

database = {} #dictionary


def init():

   
    print("Welcome to Bank PHP")
 
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else:
        print("You have selected invalid option")
        init()


def login():
    
    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
            else:
                print('Invalid account or password')
                login()
    

def validEmail(email):
    
    if '@' in email and email.count('@') == 1 and email[0].isalnum:
        pass 
    else:
        print("Invalid email")
        register()

def strongPassword(password):

    strong = False

    while strong == False:
        if len(password) >= 8:
            strong = True
        else:
            print("Passwordd should be atleast 8 characters")
            password = input("create a password (it should be atleast 8 characters) \n")


def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    validEmail(email)
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password (it should be atleast 8 characters) \n")
    strongPassword(password)
    accountBalance = 0    #added account balance to the user details

    global accountNumber
    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password, accountBalance ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )
    print("What would you like to do? \n(1) deposit \n(2) withdrawal \n(3) Balance \n(4) Logout \n(5) Exit")

    selectedOption = int(input(""))

    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation()
    elif(selectedOption == 3):
        
        print("Account balance:", database[accountNumber][4])
        bankOperation(database[accountNumber])
    elif(selectedOption == 4):
        
        logout()
    elif(selectedOption == 5):
        
        exit()
    else:
      
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    withdrawalAmount = (input("Enter amount in Naira:\n"))

    if withdrawalAmount.isdigit:
        withdrawalAmount = float(withdrawalAmount)
        pass
    else:
        print("Please Enter Numerics")
        withdrawalOperation()
    
    if withdrawalAmount > database[accountNumber][4]:
        print("Insufficient fund")
        bankOperation(database[accountNumber])

    print("Please Take Your Cash")

    database[accountNumber][4] -= withdrawalAmount

    bankOperation(database[accountNumber])

def depositOperation():
    depositAmount = (input("Enter amount in Naira:\n"))

    if depositAmount.isdigit:
        depositAmount = float(depositAmount)
        
    else:
        print("Please Enter Numerics")
        depositOperation()
    print("Please make payment")
    print("*** Loading...")
    print("Deposit of %2g was successful" %depositAmount)
    
    database[accountNumber][4] += depositAmount

    bankOperation(database[accountNumber])                 #Return to bank operations



def generationAccountNumber():

    accountNumber = int('646' + str(random.randrange(11111111,99999999)))
    return accountNumber

def logout():
    login()

#### ACTUAL BANKING SYSTEM #####

init()