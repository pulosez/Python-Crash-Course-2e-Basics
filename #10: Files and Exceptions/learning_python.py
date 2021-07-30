file_name = 'text_files/learning_python.txt'

# 10.1.
with open(file_name) as file_object:
    contents = file_object.read()
print(contents.rstrip())

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

# 10.2.
with open(file_name) as file_object:
    for line in file_object:
        message = line.replace('Python', 'C#')
        print(message.rstrip())
