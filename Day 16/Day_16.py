
with open ("input.txt", "r") as myfile:
    lines = myfile.read().split('\n\n')
    #input = [line.replace('\n', ' ').rstrip(' ').split(' ') for line in lines]

for line in lines:
    print(line)
# keys = [[field.split(':')[0] for field in line] for line in input]
# values = [[field.split(':')[1] for field in line] for line in input]
# dic = [[field.split(':') for field in line] for line in input]
