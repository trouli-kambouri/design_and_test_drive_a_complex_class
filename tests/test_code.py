from lib.code import *

'''
first test:

create an instance of the class BirthdayRecords
def person_1_birthday = BirthdayRecords(self.name, self.birthday)
assert self.birthday_dict() == person_1_name, person_1_birthday
'''

def test_person_1_creation():

    person_1 = BirthdayRecords("Gordon", 11/3/1963)
    person_1.add_to_dictionary("Gordon", 11/3/1963)

    assert person_1.birthday_dict() == "Gordon", 11/3/1963