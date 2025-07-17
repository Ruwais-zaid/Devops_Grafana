import json

with open('C:\Users\hp\OneDrive\Desktop\docker-assingment\logs\robot.json', 'r') as f:
    data = json.load(f)

with open('./robot.log', 'w') as f:
    for entry in data:
        f.write(json.dumps(entry) + '\n')
