
class BirthdayRecords():

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.birthday_dict = {}
    
    def add_to_dictionary(self):
        self.birthday_dict.update({self.name: self.birthday})
        
