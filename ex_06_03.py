def count(word, find_letter):
    counter = 0
    for letter in word:
        if letter == find_letter:
            counter = counter + 1
    return counter
