class Person:
    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address

    def print(self):
        print(f"{self.name}, born on {self.birthday}")
        print(f"Residing at: {self.address}")


# Example from the exercise:
p1 = Person("John Doe", "06/03/2000", "Beethovenstr. 1, 73430 Aalen")
p1.print()
