# 10.(8, 9).
file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    try:
        print(f"Try to open file {file_name} ...")
        with open(file_name) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        # print(f"Sorry, it looks file {file_name} is not found.")
        pass
