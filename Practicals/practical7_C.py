# c) to write a python program to count the number of words in file
with open("file2.txt", "r") as f:
    word_dict = {}
    for line in f:
        line = line.strip()
        line = line.lower()
        word = line.split(' ')
        for w in word:
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1

    words=sum(word_dict.values())
    print(f"Total Words Are {words}")