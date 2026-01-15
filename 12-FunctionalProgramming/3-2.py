text = 'I completely agree with you'

# 1. Split the text into a list of words
words = text.split()

# 2. Use map() and a lambda function to get the length of each word
word_lengths = list(map(lambda word: len(word), words))

print(word_lengths)
# Output: [1, 10, 5, 4, 3]