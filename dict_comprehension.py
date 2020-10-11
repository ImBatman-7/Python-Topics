square = {f"square of {num} is" : num**2 for num in range(1,11)}
for i, j in square.items():
    print(f"{i} : {j}")


name = "Abhinav Sahu"
word_count = {char:name.count(char) for char in name}
print(word_count)


odd_even = {i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)


# SETS COMPREHENSION

s = {i**2 for i in range(1,11)}
print(s)
