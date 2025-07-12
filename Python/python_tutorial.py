# Python Tutorial: Fundamental Concepts

# 1. Variables and Data Types
name = "Alice"         # String
age = 25               # Integer
height = 5.7           # Float
is_student = True      # Boolean

# 2. Printing Output
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student?", is_student)

# 3. Basic Arithmetic Operations
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# 4. Lists (Arrays)
fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])
fruits.append("orange")    # Add item
print("All fruits:", fruits)

# 5. Tuples (Immutable Sequences)
point = (2, 3)
print("X coordinate:", point[0])

# 6. Dictionaries (Key-Value Pairs)
person = {"name": "Bob", "age": 30}
print("Person's name:", person["name"])

# 7. Conditional Statements
if age >= 18:
    print("Adult")
else:
    print("Minor")

# 8. Loops
# For loop
for fruit in fruits:
    print("Fruit:", fruit)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# 9. Functions
def greet(name):
    """Function to greet a person."""
    print("Hello,", name)

greet("Alice")

# 10. Classes and Objects
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says woof!")

my_dog = Dog("Buddy")
my_dog.bark()