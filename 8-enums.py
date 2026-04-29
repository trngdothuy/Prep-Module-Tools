# Write a program which:

# Already has a list of Laptops that a library has to lend out.
# Accepts user input to create a new Person - it should use the input function to read a person’s name, age, and preferred operating system.
# Tells the user how many laptops the library has that have that operating system.
# If there is an operating system that has more laptops available, tells the user that if they’re willing to accept that operating system they’re more likely to get a laptop.
# You should convert the age and preferred operating system input from the user into more constrained types as quickly as possible, and should output errors to stderr and terminate the program with a non-zero exit code if the user input bad values.

from dataclasses import dataclass
from enum import Enum
from typing import List
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem


@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem


def find_possible_laptops(laptops: List[Laptop], person: Person) -> List[Laptop]:
    possible_laptops = []
    for laptop in laptops:
        if laptop.operating_system == person.preferred_operating_system:
            possible_laptops.append(laptop)
    return possible_laptops


laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
]
 
# name from user input   
name = input("Enter your name: ")
# age from user input 
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age", file=sys.stderr)
    sys.exit(1)
    
# os from user input 
os_input = input("Preferred OS (macOS/Ubuntu/Arch Linux): ")

if os_input.lower() == "macos":
    preferred_os = OperatingSystem.MACOS
elif os_input.lower() == "ubuntu":
    preferred_os = OperatingSystem.UBUNTU
elif os_input.lower() == "arch linux":
    preferred_os = OperatingSystem.ARCH
else:
    print("Invalid operating system", file=sys.stderr)
    sys.exit(1)

person = Person(name, age, preferred_os)

# count matching laptops
count = 0
for laptop in laptops:
    if laptop.operating_system == person.preferred_operating_system:
        count += 1
print(f"We have {count} laptop(s) with {person.preferred_operating_system.value}")

# count laptop per os
mac_count = 0
ubuntu_count = 0
arch_count = 0

for laptop in laptops:
    if laptop.operating_system == OperatingSystem.MACOS:
        mac_count += 1
    elif laptop.operating_system == OperatingSystem.UBUNTU:
        ubuntu_count += 1
    elif laptop.operating_system == OperatingSystem.ARCH:
        arch_count += 1
        
# suggest better option:
best_os = OperatingSystem.MACOS
best_count = mac_count

if ubuntu_count > best_count:
    best_os = OperatingSystem.UBUNTU
    best_count = ubuntu_count

if arch_count > best_count:
    best_os = OperatingSystem.ARCH
    best_count = arch_count
    
if best_os != person.preferred_operating_system:
    print(f"If you are willing to use {best_os.value}, you're more likely to get a laptop")
