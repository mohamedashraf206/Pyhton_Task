from user import user
from projects import Project
import json
import re
# function validInput {
#   # this function taske two argument the first is a string you want to check and the second is a regex

#   read -r input
#   echo " ***********************************"

#   while ! [[ $input =~ ${1} ]]; do
#     echo "please enter a valid input"
#     read -r input
#     echo " ***********************************"

#   done

# }
def ValidateInput(regex):
    userInput = input("")
    regex = r'' + regex
    while not(bool((re.match(regex, userInput)))):
        userInput = input("plaease enter a valid input\n")
    
    return userInput





def saveUser(thing):
    with open("user.json", "w") as f:
        json.dump([p.__dict__ for p in thing], f, indent=4)
    

def loadUser():
    # Retrieve the objects from the file
    with open("user.json", "r") as f:
        user.users = [user(**p) for p in json.load(f)]
        
        
        
def saveProject(thing):
    with open("projects.json", "w") as f:
        json.dump([p.__dict__ for p in thing], f, indent=4)
        print("saved")
    

def loadProject():
    # Retrieve the objects from the file
    with open("projects.json", "r") as f:
        Project.projects = [Project(**p) for p in json.load(f)]
        print(Project.projects[0].title)




def register():
    print("enter Fname \n")
    fName=ValidateInput("^[a-zA-Z]{3,}$")
    print("enter lname\n")
    lName=ValidateInput("^[a-zA-Z]{3,}$")
    print ("Enter your email \n")
    email=ValidateInput("^[a-zA-Z0-9]{4,}@(gmail|outlook)\.com$")
    print("enter your password\n")
    password =ValidateInput("^[a-zA-Z0-9\!\@\#\$\%\^\&\(\)\_\+\=\~]{8,}$") 
    print ("Enter your phone number\n")
    mobile=ValidateInput("^(010|011|012|015)[0-9]{8,}$")
    usr=user(fName,lName,email,password,mobile)
    user.users.append(usr)
    saveUser(user.users)
def createProject():
    owner=user.users[0].id
    title=input("project title")
    details=input("details")
    total_target=input("total_target")
    start_date=input("start_date")
    end_date=input("end_date")
    pro1=Project(owner,title, details, total_target, start_date, end_date)
    print(pro1.title)
    Project.projects.append(pro1)
    saveProject(Project.projects)
