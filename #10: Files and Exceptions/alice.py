def count_words(filename):
    """Порахувати приблизну кількість слів у файлі."""
    try:
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {file_name} does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has about {num_words} words.")


file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file_name in file_names:
    count_words(file_name)
