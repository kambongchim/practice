import json
import requests
from pprint import pp
#serializing
# dump() write data to a file like object in json format
#dumps () write data to string in json format
# open() in a try and except block
# with open() as 

data = {
    'user': {
        "name": "Will William", 
        'age': 93}
        }

#print(data['user']['age'])

with open("Data_file.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)

json_str =  json.dumps(data, indent = 4)
print(json_str)

#check and see if serializaiton and deserializationa re perfect inverses
blackJack = (8, "Q")
encoded = json.dumps(blackJack)
decoded = json.loads(encoded)

print(type(blackJack), type(decoded))
print(blackJack == tuple(decoded))

#deserialization example
response = requests.get("http://jsonplaceholder.typicode.com/todos")
todos =  json.loads(response.text)
print(type(todos))
#pp(todos[:10])

#see who has most completed items

todosByUsers = {}
for item in todos:
    if item['completed'] == True:
        if item['userId'] not in todosByUsers.keys():
            todosByUsers[item['userId']] = 1
        else:
            todosByUsers[item['userId']] += 1

#print(todosByUsers)

top_users = sorted(todosByUsers.items(), key = lambda x: x[1], reverse = True )
#print(top_users)

maxComplete = top_users[0][1]
print(maxComplete)

stars = [x for x,y in top_users if y == maxComplete]
stars2 = []
for user, val in top_users:
    if val == maxComplete:
        stars2.append(user)
print(stars2)

print(f'User(s) {stars[0]} completed {stars[1]} TODOs')

def kepp(todos):
    isComplete = todos['completed']
    hasMaxCount = str(todos['userId']) in user
    return isComplete and hasMaxCount

with open('filter_data_file.json', 'w') as data_file:
    filterTodos = list(filter(kepp, todos))
    json.dump(filterTodos, data_file, indent = 2)
