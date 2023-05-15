import json

with open('projects.json', 'r') as f:
    print(json.load(f))