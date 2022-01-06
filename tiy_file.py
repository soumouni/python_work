#try it yourself 10-1
#page 191
file_name='learning_python.txt'
print("FIRST PRINT\n")
#by reading entire file
with open(file_name) as file_object:
    content=file_object.read()
print(content)

#by looping over the file object
print()
print("SECOND PRINT\n")
with open(file_name) as file_object:
    for line in file_object:
        print(line.strip())

#by storing the lines in a list and then working with them outside the with block
print()
print("THIRD PRINT\n")
with open(file_name) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.strip())

#10-2 Learning C
print("replacing python with C\n")
with open(file_name) as file_object:
    content=file_object.read()
content=content.replace('python', 'C')
print(content)