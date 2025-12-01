def f(word):
    final_word = ''
    for i in word:
        final_word += i + '-'
    return final_word[0:-1]


if __name__ == '__main__':
    print(f('University'))
    print(f('x'))
    print(f(''))