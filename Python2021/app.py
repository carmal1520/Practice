# # count = 0
# # for x in range(1, 10):
# #     if x % 2 == 0:
# #         count = count + 1
# #         print(x)
# # print(f"We have {count} even numbers")

# # def love():
# #     love = False
# #     if love:
# #         print("I love you")
# #     else:
# #         print("lmao get out," + " we them boys")
# # love()

# # def amazon_employee(f_name, l_name):
# #     print(f"Hello {f_name} {l_name} ")
# # amazon_employee("Carlos", "Maldo")

# # def x(a, b):
# #     return a + b
# # print(x(a=2, b=3))

# # def number(x, y=5):
# #     return x + y
# # print(number(5, -4))

# # def multiply(*numbers):
# #     # total = 0
# #     for number in numbers:
# #         # total = total * number
# #         return numbers
# # print(multiply(2,3, 4, 5))

# # def fizz_buzz(input):
# #     if input % 3 == 0 and input % 5 == 0:
# #         return("fizzbuzz")
# #     if input % 3 == 0:
# #         return("fizz")
# #     if input % 5 == 0:
# #         return("buzz")
# #     else:
# #         return input
# # print(fizz_buzz(15))

# # letters = ["a", "b", "c"]
# # # matrix = [[0, 1] [2, 3]]
# # zeros = [0] * 5
# # combined = zeros + letters
# # numbers = list("Hello World")
# # print(numbers)
# # print(combined)

# # letters = ["a", "b", "c"]
# # for a, b in enumerate(letters):
# #     print(a, b)

# ####################LAMBDA
# # def sort_item(item):
# #     return item[1]

# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 12),
# ]

# # items.sort(key=lambda item:item[1])
# # print(items)

# # prices = list(map(lambda item: item[1], items))

# # prices = [x[1] for x in items]

# # filtered = list(filter(lambda item: item[1] >= 10, items))
# # filtered = [x[0] for x in items if x[1] >= 10]
# # print(filtered)

# values = []
# for x in range(5):
#     values.append(x * 2)
#     print(values)
#     # varialbe = [expression for item in items]
#     values = [x * 2 for x in range(5)] 

# values = list(range(5))
# values = [*range(5)]
# print(values)

# sentence = "This is a common interview question"
# char_freq = {}
# for x in sentence:
#     if x in char_freq:
#         char_freq[x] += 1
#     else:
#         char_freq[x] = 1

# char_freq_sorted = sorted(char_freq.items(),key=lambda kv: kv[1], reverse=True)
# print(char_freq_sorted[0])

guest_list = ["Liam", "Russ","Jordan"]
guest_list.remove("Jordan")
guest_list.append("Carlos")
for x in guest_list:
    print("Hello " + x + " You are invited to dinner")

print("Jordan cant make it")
