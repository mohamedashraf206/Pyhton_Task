from user import *
from projects import *
import json
import re
import datetime
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




def ValidateInputDate(mes):
    userInput = input(mes)
    
    while not(validate_date(userInput)):
        userInput = input("plaease enter a valid input\n")
    
    return userInput





def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False





def saveUser(thing):
    with open("user.json", "w") as f:
        json.dump([p.__dict__ for p in thing], f, indent=4)
    

def loadUser():
    # Retrieve the objects from the file
    try:
        with open("user.json", "r") as f:
            user.users = [user(**p) for p in json.load(f)]
    except:
        print("no user was created")

        
        
        
def saveProject(thing):
    with open("projects.json", "w") as f:
        json.dump([p.__dict__ for p in thing], f, indent=4)
        print("saved")
    

def loadProject():
    # Retrieve the objects from the file
    try:
        with open("projects.json", "r") as f:
            Project.projects = [Project(**p) for p in json.load(f)]
            print(Project.projects[0].title)
    except:
        print("no project was created")




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
    mobile=ValidateInput("^(010|011|012|015)[0-9]{8,8}$")
    usr=user(fName,lName,email,password,mobile)
    user.users.append(usr)
    saveUser(user.users)
    print("user register successfully")
def createProject():
    owner=user.signed_in.id
    title=input("project title\n")
    details=input("details\n")
    total_target=input("total_target\n")
    start_date=ValidateInputDate(" enter start date\n")
    end_date=ValidateInputDate( " enter end date\n")
    pro1=Project(owner,title, details, total_target, start_date, end_date)
    print(pro1.title)
    Project.projects.append(pro1)
    saveProject(Project.projects)

def login():
    email = input ("Enter your Email \n")
    password = input ("Enter your  Password\n")
    
    for userobj in user.users :
        if email == userobj.email and password == userobj.password :
            print("You signed in successfully")
            user.signed_in = userobj
            print (userobj.signed_in.fName)
            
            return 
    print("the user not exist")

def mainMenu ():
    
    
    print("=============Main Menu==========")
    print("type 1 to login ")
    print("type  2 to register ")

    userInput  = input("Enter ") 
    if userInput ==  "1":
        login()
        projectsMenu()
    elif userInput == "2":
        register() 
        mainMenu()
    else: 
        print ("Wrong Choice")
        mainMenu()
        
        
def getProObj(project_title):
    projectobj=""
    for i in Project.projects:
        if i.title==project_title:
            projectobj=i
    return projectobj
            
def verifyOwner(projectobj):
    
    try:
        if user.signed_in.id==projectobj.owner_id:
            return True
        else:
            return False
    except:
        print("there is no such project")
        return False
        
def view():
    for i in Project.projects :
        print("****")
        print ("project title ",i.title)
        print ("project details ",i.details)
        print ("project amount collectd ",i.collected)
        print ("project total target ",i.total_target)
        print ("project start_date ",i.start_date)
        print ("project end date ",i.end_date)
        print("****")
        
    
                 
def projectsMenu():
    print("=============Projects Menu==========\n")
    print("type 1 to view projects \n")
    print("type  2 to edit your project \n")
    print("type  3 to delete your project \n")
    print("type  4 to create new project ")
    print("type  5 to donate ")
    userInput  = input("Enter ") 
    if userInput ==  "1":
        view()
        projectsMenu()
   

    elif userInput == "2":
        print("there exists these projects\n")
        for i in Project.projects :
            print("****")
            print (i.title,"\n")
            print("****")
        projectobj=getProObj(input("please enter project title\n"))
        if verifyOwner(projectobj):
            print("*********************enter new data*******************")
            title=input("project title\n")
            details=input("details\n")
            total_target=input("total_target\n")

            projectobj.title=title
            projectobj.details=details
            projectobj.total_target=total_target
            projectobj.start_date=ValidateInputDate("enter starting date")
            projectobj.end_date=ValidateInputDate("enter ending date")         
            saveProject(Project.projects)
            projectsMenu()
        else:
            print("you are not the owner so you can't modify it")
            projectsMenu()
        
        
        
        
    elif userInput ==  "3":
        print("there exists these projects")
        for i in Project.projects :
            print("****")
            print (i.title,"\n")
        projectobj=getProObj(input("please enter project title\n"))
        if verifyOwner(projectobj):
            Project.projects.remove(projectobj)
            saveProject(Project.projects)
            projectsMenu()
        else:
            print("you are not the owner")
            projectsMenu()











    elif userInput ==  "4":
        createProject()
        projectsMenu()
    elif userInput ==  "5":
        for i in Project.projects :
            print("****")
            print (i.title,"\n")
            print("amout collected: ",i.collected,"\n")
            print("target: ",i.total_target,"\n")
        obj= getProObj(input("enter project title to donate\n"))
        try:
            print("amout collecte: ",obj.collected,"\n")
            print("target: ",obj.total_target,"\n")
            donate = int(input("please enter donation amout "))
            obj.collected+=donate
            print("amout collecte: ",obj.collected,"\n")
            print("target: ",obj.total_target,"\n")
        except:
            print("there is no project with this title")
        projectsMenu()
            
    else: 
        print ("Wrong Choice")
        mainMenu()










                            