with open ("input.txt", "r") as myfile:
    lines = myfile.read().split('\n\n')
    input = [line.replace('\n', ' ').rstrip(' ').split(' ') for line in lines]

keys = [[field.split(':')[0] for field in line] for line in input]
values = [[field.split(':')[1] for field in line] for line in input]
dic = [[field.split(':') for field in line] for line in input]


def validate(passport):
    if(len(passport) == 8):
        return 1
    elif(('cid' in passport) and (len(passport) < 8)):
        return 0
    elif(('cid' not in passport) and (len(passport) < 7)):
        return 0
    else:
        return 1

def validatePartTwo(passport, values):
    if(len(passport) == 8):
        return 1
    elif(('cid' in passport) and (len(passport) < 8)):
        return 0
    elif(('cid' not in passport) and (len(passport) < 7)):
        return 0
    else:
        return 1

count = 0
for passport in keys:
    count += validate(passport)

countTwo = 0
for i in range(len(keys)):
    countTwo += validatePartTwo((keys[i], values[i]))

print(count)