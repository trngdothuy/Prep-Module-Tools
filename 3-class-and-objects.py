class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str, address: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system
        self.address = address

imran = Person("Imran", 22, "Ubuntu", "123 Street")
print(imran.name)
print(imran.address)

eliza = Person("Eliza", 34, "Arch Linux", "ABX District")
print(eliza.name)
print(eliza.address)

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))

# Write a new function in the file that accepts a Person as a parameter and tries to access a property that doesn’t exist. Run it through mypy and check that it does report an error.

def isMale(person: Person) -> bool:
    return person.gender == "male"

# Returns:
# 3-class-and-objects.py:24: error: Returning Any from function declared to return "bool"  [no-any-return]
# 3-class-and-objects.py:24: error: "Person" has no attribute "gender"  [attr-defined]
# Found 2 errors in 1 file (checked 1 source file)