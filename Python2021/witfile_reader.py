# # Print content by reading entire file
# with open('learning_python.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# # Print content by looping over the file object
# with open('learning_python.txt') as file_object:
#     for line in file_object:
#         print(line)

# # Print content by storing the lines in a list and then working with them outside the with block
# with open('learning_python.txt') as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.replace('Python', 'Java')) #replace Python with Java with replace() method

