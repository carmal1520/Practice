filename = 'cats2.txt'
try:
    with open(filename, encoding='utf-8') as x:
        content = x.read()
except FileNotFoundError:
    pass
else:
    print(content)