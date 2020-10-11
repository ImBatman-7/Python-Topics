user = {}

name = input('what is your name : ')
age = int(input('what is your age : '))
songs = input('tell your two favourite songs comma seperated : ').split(',')
movies = input('tell your two favourite movies comma seperated : ').split(',')

user['name'] = name
user['age'] = age
user['songs'] = songs
user['movies'] = movies

for key, value in user.items():
    print(f'{key} : {value}')
