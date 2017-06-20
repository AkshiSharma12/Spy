from datetime import datetime
#imports datetime class from datetime file

class Spy:
    #class created for spy details

    def __init__(self, name, salutation, age, rating):
        #creates a constructor
        #self keyword is used to store values in the constructor
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    #class created for storing,appending and printing the chats

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        #datetime.now() acceses the current system date and time
        self.sent_by_me = sent_by_me

spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('Damon', 'Mr.', 4.9, 27)
friend_two = Spy('Katherine', 'Ms.', 4.39, 21)
friend_three = Spy('Grey', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]

