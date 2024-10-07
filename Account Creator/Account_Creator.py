import re


def generateUsername(fullName, startYear):
    #this subroutine will generate the username 
    #based on the students' first name, last name 
    #and their starting year
          
    fullName.capitalize()
    firstName, lastName = fullName.split(" ")
    username = startYear[-2:] + lastName + firstName[0] 
    print(username)
    print(lastName)
    print(firstName)
    return username

def calculateYearGroup(username):
    #this subroutine will calculate the year group
    #that the student is in based on their username
    
    userNumber = username[0:2]
    if userNumber == "24":
        yearGroup = "Year 7"
    elif userNumber == "23":
        yearGroup = "Year 8"
    elif userNumber == "22":
        yearGroup = "Year 9"
    elif userNumber == "21":
        yearGroup = "Year 10"
    elif userNumber == "20":
        yearGroup = "Year 11"
    elif userNumber == "19":
        yearGroup = "Year 12"
    return yearGroup

def getPassword(username):
    #this subroutine will ask the user to enter a password 
    #and pass it to the isPasswordSecure subroutine to 
    #check if it is secure
    password = input("enter a password: ")
    while isPasswordSecure(password, username) == False:
        password = input("password was not secure, please try again: ")
    return password

def isPasswordSecure(password, username):
    if re.search(username, password):
        print("Password must not contain the username.")
        return False
    if re.search(r"password", password):
        print("Password must not be 'password'.")
        return False
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter.")
        return False
    if not re.search(r"\d", password):
        print("Password must contain at least one digit.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>'+-_=~]", password):
        print("Password must contain at least one special character.")
        return False
    
    return True

def menu():
    fullName = input("enter your full name (first and last name separated by a space): ")
    startYear = input("enter your starting year (e.g. 2024):")
    username = generateUsername(fullName, startYear)
    yearGroup = calculateYearGroup(username)
    password = getPassword(username)
    
#menu()