names = ['thiruvanantrhapuram', 'thirukkal', 'pondicherry']
for i, j in enumerate(names):
    print(f'{i}------>{j}')

# _____________________________________

def find_pos(l, target):
    for pos, name in enumerate(l):
        if name==target:
            return pos
        else:
            return -1

names = ['abhinav', 'sahu', 'gulmarg'] 
print(find_pos(names, 'abhinav'))



