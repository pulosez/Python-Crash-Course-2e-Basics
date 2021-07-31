# 10.10.
def count_common_words(file, word='the'):
    try:
        with open(file, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        num_words = contents.lower().count(word)
        print(f"The word '{word}' appears in {file} {num_words} times.")


file_name = 'alice.txt'
count_common_words(file_name)
