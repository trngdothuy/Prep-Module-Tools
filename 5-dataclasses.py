# Write a Person class using @datatype which uses a datetime.date for date of birth, rather than an int for age.
# Re-add the is_adult method to it.

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    dob: date
    preferred_operating_system: str
    
    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.dob.year 
        
        # not yet bday -> minus 1 in age
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
                   
        return age >= 18

imran = Person("Imran", date(2000, 1, 2), "Ubuntu")  # We can call this constructor - @dataclass generated it for us.
print(imran)  

imran2 = Person("Imran", date(2001, 1, 2), "Ubuntu")
print(imran == imran2)  

print(imran.is_adult())