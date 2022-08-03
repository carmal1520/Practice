filename = 'Chambers.txt'

with open(filename, encoding = 'utf-8') as x:
    contents = x.read()
    total = contents.lower().count('the ')
    print(total)