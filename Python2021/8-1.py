# 8-1
# def display_message():
#     """This is a test"""
#     print("I learned about functions in this chapter")

# display_message()

# 8-2
# def favorite_book(book_title):
#     print(f"My favorite book is {book_title.title()}.")

# favorite_book("jungle BOOK")

# 8-3
# def make_shirt(shirt_message, shirt_size ='large'):
#     print(f"\n1The size of the shirt is: {shirt_size}.")
#     print(f"The message of the shirt is: \n\t{shirt_message}.")
# make_shirt('I love python')
# make_shirt('default message')
# make_shirt(shirt_size='medium', shirt_message='get off')
# make_shirt(shirt_size ='small', shirt_message = 'I like movies')

# 8-5
# def describe_city(city, country='United States'):
#     print(f'\n{city} is located in {country}')
# describe_city('Tokyo', country='Japan')
# describe_city('Virginia Beach')
# describe_city('Manila', country='Phillipines')

# 8-6
# def city_country(city, country):
#     full_list = f"{city} , {country}"
#     return full_list.title()
# city1 = city_country('New York', 'United States').capitalize()
# city2 = city_country('Tokyo', 'Japan').title()
# city3 = city_country('Virginia Beach', 'United States').title()
# print(city1)
# print(city2)
# print(city3)

# 8-7
# music = make_album('Michael Jackson', 'Thriller')
# music2 = make_album('FatRat', 'Mecha', 50)
# music3 = make_album('Anjulie', 'KSHMR')
# print(music)
# print(music2)
# print(music3)

# def make_album(artist_name, album_title, song_number=None):
#     """Returning a Dictionary"""
#     artist = {'name' : artist_name, 'album' : album_title}
#     if song_number:
#         artist[song_number] = song_number
#     return artist


# while True:
#     print('Please enter an Artist Name and Artist Album: ')
#     print('Type "Quit" to leave anytime')
#     artist_name = input("Artist Name: ")
#     if artist_name == 'Quit':
#         break
#     album_title = input("Artist Album: ")
#     if album_title == 'Quit':
#         break
#     x = make_album(artist_name, album_title)
#     print(x)
 
# 8-9
# def show_messages(texts):
#     for text in texts:
#         msg = f"{text.upper()}"
#         print(msg)

# text_messages = [
#     "Hello world",
#     "Video games are fun",
#     "I love python"
# ]

# show_messages(text_messages)

# 8-10
# sent_messages = []
# text_messages = [
#     "Hello world",
#     "Video games are fun",
#     "I love python"
# ]
# def show_messages(text_messages, sent_messages):
#     while text_messages:
#         text_message = text_messages.pop()
#         print(f"Sending {text_message}")
#         sent_messages.append(text_message)

# def send_messages(sent_messages):
#     print("\nThe following messages were sent: ")
#     for send_message in sent_messages:
#         print(send_message)

# show_messages(text_messages, sent_messages)
# send_messages(sent_messages)

# 8-11
sent_messages = []
text_messages = [
    "Hello world",
    "Video games are fun",
    "I love python"
]
def show_messages(text_messages, sent_messages):
    while text_messages:
        text_message = text_messages.pop()
        print(f"Sending {text_message}")
        sent_messages.append(text_message)

def send_messages(sent_messages):
    print("\nThe following messages were sent: ")
    for send_message in sent_messages:
        print(send_message)

show_messages(text_messages[:], sent_messages)
send_messages(sent_messages)
print(f"\n{text_messages}")