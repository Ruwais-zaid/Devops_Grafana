import json

with open(r'C:\Users\hp\OneDrive\Desktop\docker-assingment\logs\robot.json', 'r') as f:
    data = json.load(f)

with open(r'C:\Users\hp\OneDrive\Desktop\docker-assingment\logs\robot.log', 'w') as f:
    for entry in data:
        f.write(json.dumps(entry) + '\n')
