"""
CTEC 121
Ilya
Mod 5 Lab 2
class demos
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
# Lab exercise 1
"""
def verse(name):
    print(name, "finger,", name, "finger, where are you?")

def refrain():
    print("Here I am, Here I am. How do you do?")

def main():
    verse("Daddy")
    refrain()
    print()
    verse("Mommy")
    refrain()
    print()
    verse("Brother")
    refrain()
    print()
    verse("Sister")
    refrain()
    print()
    verse("Baby")
    refrain()
    print()
"""

# Lab exercise 2

def func(age):
    if age < 2:
        return "I"
    elif age < 13:
        return "C"
    
def unitTest():
    print(func(1))
    print(func(7))


unitTest()    