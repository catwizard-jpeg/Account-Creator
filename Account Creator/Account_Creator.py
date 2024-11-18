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
     yearGroups = {
         "24": "Year 7",
         "23": "Year 8",
         "22": "Year 9",
         "21": "Year 10",
         "20": "Year 11",
         "19": "Year 12",
         "18": "Year 13"
     }
     yearGroup = yearGroups.get(userNumber, "Unknown") #if the userNumber is not in the dictionary, return "Unknown"
     
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
    
menu()