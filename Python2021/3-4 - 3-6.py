dinner_list = ['eric', 'liam', 'russ']
# print(f"You are invited to dinner {dinner_list[0]}")
# print(f"You are invited to dinner {dinner_list[1]}")
# print(f"You are invited to dinner {dinner_list[2]}")
dinner_list.pop()
dinner_list.append("caren")
print("russ said he cant make it to dinner")
print(f"You are invited to dinner {dinner_list[0]}")
print(f"You are invited to dinner {dinner_list[1]}")
print(f"You are invited to dinner {dinner_list[2]}")
print('We have', len(dinner_list), 'guest coming to dinner')