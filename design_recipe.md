# 1. user cases


As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

# 2. Functions


class BirthdayRecords():
    def __init__(self, name, birthday):
        
        self.name = name
        self.birthday = birthday
        self.birthday_dict = {}
    
    def update_birthday(self, new_birthday):

        self.birthday_dict.update({"name"}: new_birthday)

    def update_name(self, new_name):

        self.birthday_dict.update(new_name: {birthday})
        LOOK UP HOW TO CHANGE KEY
    
    find upcoming birthdays:
        from datetime import date
        current date + 1 - 06/06/2015
    pass

3. Test examples

