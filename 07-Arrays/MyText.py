def number_of_words(x):
    words = x.split()
    counter = 0
    for i in words:
        counter += 1
    return counter

def sorting(x):
    words = x.split()
    return sorted(words, key=len, reverse=True)

def sort_alphabetically(text):
    words = text.split(" ")
    return sorted(words, key=str.lower)



