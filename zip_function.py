user_id = ['user1', 'user2', 'user3']
names = ['abhinav', 'sinister', 'conjure']

print(list(zip(user_id, names)))

# ____________________________________

user_id = ['user1', 'user2']
names = ['abhinav', 'sinister', 'conjure']

print(list(zip(user_id, names)))

# ______________________________________

user_id = ['user1', 'user2', 'user3']
names = ['abhinav', 'sinister', 'conjure']

print(dict(zip(user_id, names)))



# ______________________________________



l1 = [1,2,3,4]
l2 = [5,1,7,8]

new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
   

print(new_list)    



# return average

# def average_finder(*args):
#     average = []
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average

# print(average_finder([1,2,3,4], [5,1,7,8]))        


average_finder = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3,4], [5,1,7,8]))        