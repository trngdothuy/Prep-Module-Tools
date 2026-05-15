# Exercise: Think of the advantages of using methods instead of free functions. Write them down in your notebook.
# ---> Answer: Methods are functions linking to a class or object, so using them can be better in:
# - organizing and easy to understand
# - data encapsulation, easier to manage behavior as it's closer to the data used
# - reusability and scalability, especially when extending
# - reducing repeating parameters

# Ex 2: Change the Person class to take a date of birth (using the standard library’s datetime.date class) and store it in a field instead of age.
# Update the is_adult method to act the same as before.

from datetime import date

class Person:
    def __init__(self, name: str, dob: date, preferred_operating_system: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.dob.year     
        
        # not yet bday -> minus 1 in age
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
               
        return age >= 18

imran = Person("Imran", date(2008, 12, 12), "Ubuntu")
print(imran.is_adult())