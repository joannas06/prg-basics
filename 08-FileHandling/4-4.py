
def firstfivelines(company):
    with open(company) as file:
        content = file.read()
    return content

file = firstfivelines("it_company.csv")
file_lines = file.splitlines()

for line in file_lines[0:5]:
    x = str(input('Write enter!: '))
    print(file_lines[0:5])