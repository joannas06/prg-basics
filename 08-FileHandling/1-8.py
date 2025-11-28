def read_from_file(name):
    with open(name) as file:
        content = file.read()
        return content
    
file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()
line_words = file_lines.split()
amt_of_words = len(line_words)









