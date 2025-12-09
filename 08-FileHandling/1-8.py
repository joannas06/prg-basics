def read_from_file(name):
    with open(name) as file:
        content = file.read()
        return content
    
file_content = read_from_file('pets.txt')
line_words = file_content.split()
amt_of_words = len(line_words)

print(amt_of_words)
print(read_from_file('pets.txt'))









