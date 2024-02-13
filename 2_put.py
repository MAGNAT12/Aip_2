import requests


data = {
    'userId': 1,
    'id': 5,
    'title': 'updated resource',
    'completed': True
}
respons = requests.put("https://jsonplaceholder.typicode.com/todos/5",  data=data)

print(respons.text)
