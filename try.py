# from functions import *

# import json

# def append_data_to_json_file (data):
#     with open("data.json", "a") as f:
#         json.dump(data, f)
#         f.write("\n")
        
        
        
# data = {"name": "Alice", "age": 30}
# append_data_to_json_file(data)


# import json

# def read_data_from_json_file():
#     with open("data.json", "r") as f:
#         data = []
#         for line in f:
#             data.append(json.loads(line))
#     return data


# data = read_data_from_json_file()
# print(data)











import json

class Project:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

def load_projects():
    with open('project.json', 'r') as f:
        loaded_projects = [Project(**p) for p in json.load(f)]
    return loaded_projects

def add_project(name, description, status):
    new_project = Project(name, description, status)
    with open('project.json', 'a') as f:
        f.write("["+json.dumps(new_project.__dict__) + ']\n')
        
        
add_project('Project a', 'This is project C', 'in progress')
add_project('Project b', 'This is project C', 'in progress')
add_project('Project C', 'This is project C', 'in progress')

loaded_projects = load_projects()

# print the loaded projects
for project in loaded_projects:
    print(project.name, project.description, project.status)

# add a new project to the file
add_project('Project C', 'This is project C', 'in progress')

# reload the projects from the file
loaded_projects = load_projects()

# print the updated list of projects
for project in loaded_projects:
    print(project.name, project.description, project.status)



# loadUser()
# register()

# loadUser()
# createProject()
# loadProject()


# class Project:fgfd
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

# # Create some sample Project objects
# projects = [Project("Project 1", 1), Project("Project 2", 2), Project("Project 3", 3)]

# # Save the objects to a file
# with open("projects.json", "w") as f:
#     json.dump([p.__dict__ for p in projects], f, indent=4)

# # Retrieve the objects from the file
# with open("projects.json", "r") as f:
#     loaded_projects = [Project(**p) for p in json.load(f)]

# # Print the loaded objects
# for project in loaded_projects:
#     print(project.name, project.id)








