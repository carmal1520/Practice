filename = 'learning_python_again.txt'
print("Reading the entire file:")
with open(filename) as x:
    contents = x.read()
print(contents)

print("\nLooping over the lines:")
with open(filename) as x:
     for line in x:
         print(line.rstrip())

print("\nSotring the lines in a list:")
with open(filename) as x:
    lines = x.readlines()

for line in lines:
    print(line.rstrip())