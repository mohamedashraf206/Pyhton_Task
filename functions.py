from user import user
from projects import Project
import json

def saveUser(thing):
    with open("user.json", "a") as f:
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
    fName=input("first name")
    lName=input("last name")
    email=input("email")
    password=input("password")
    mobile=input("mobile")
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
