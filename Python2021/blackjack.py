import random
from traceback import print_list


user_cards = []
computer_cards = []

def deal_card():
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   card = random.choice(cards)
   return card
print(deal_card())

# user_cards.append(deal_card())
# user_cards.append(deal_card())
# computer_cards.append(deal_card())
# computer_cards.append(deal_card())

user_cards = [deal_card() for x in range(2)]
computer_cards = [deal_card() for x in range(2)]
print(user_cards)
print(computer_cards)