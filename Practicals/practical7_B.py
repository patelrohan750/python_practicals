# B) to write a python program to find the most fequent words from file
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


    large = max(word_dict.values())
    # print(large)

    key_list = list(word_dict.keys())
    values_list = list(word_dict.values())

    fequent_word=key_list[(values_list.index(large))]
    # print(fequent_word)
    print(f"most frequent word is: {fequent_word} are  {large} times")
