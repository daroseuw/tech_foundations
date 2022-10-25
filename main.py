from another_file import add

print(add(4, 5))

with open('animals.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)