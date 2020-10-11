number = []
for i in range(1,11):
    number.append(i**2)
print(number)    

new_number = [i**2 for i in range(1,11)]
print(new_number)


new_negative = [-i for i in range(1,11)]
print(new_negative)


names = ['abhinav', 'sahu', 'manoj']
new_names = [i[0] for i in names]
print(new_names)


reversed_names =[i[::-1] for i in names]
print(reversed_names)



n2 = [i for i in list(range(1,11)) if i%2 == 0]
print(n2)

n3 = [i for i in range(1,11) if i%2 != 0]
print(n3)


any_list = [i**2 if i%2 == 0 else -i for i in range(1,21)]
print(any_list)

nested = [[i for i in range(1,4)]for j in range(3)]
print(nested)