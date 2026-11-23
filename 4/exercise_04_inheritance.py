# Exercise 4 - Inheritance
# Aalen University - Computer Science 2

import math


# ============================================================
# 4.1 Time and Duration
# ============================================================

class TimeValue:
    """
    Base class for values that contain hours, minutes and seconds.
    The attributes are shared by Time and Duration through inheritance.
    """

    def __init__(self, hours=0, minutes=0, seconds=0):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self._normalize()

    def _normalize(self):
        total_seconds = (
            self.hours * 3600
            + self.minutes * 60
            + self.seconds
        )

        self.hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        self.minutes = remaining_seconds // 60
        self.seconds = remaining_seconds % 60

    def total_seconds(self):
        return (
            self.hours * 3600
            + self.minutes * 60
            + self.seconds
        )

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"


class Time(TimeValue):
    """
    Represents a point in time.
    """

    pass


class Duration(TimeValue):
    """
    Represents a duration.
    """

    pass


# ============================================================
# 4.2 Applying Inheritance - Animals
# ============================================================

class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Mammal(Animal):
    def __init__(self, name, age, weight, fur_color, number_of_legs):
        super().__init__(name, age, weight)
        self.fur_color = fur_color
        self.number_of_legs = number_of_legs


class Bird(Animal):
    def __init__(self, name, age, weight, wingspan, ability_to_fly):
        super().__init__(name, age, weight)
        self.wingspan = wingspan
        self.ability_to_fly = ability_to_fly


class Reptile(Animal):
    def __init__(self, name, age, weight, scale_type, cold_bloodedness):
        super().__init__(name, age, weight)
        self.scale_type = scale_type
        self.cold_bloodedness = cold_bloodedness


# ============================================================
# Example usage
# ============================================================

if __name__ == "__main__":

    # 4.1
    time = Time(14, 35, 20)
    duration = Duration(2, 45, 10)

    print("4.1 Time and Duration")
    print("Time:", time)
    print("Duration:", duration)
    print("Time in seconds:", time.total_seconds())
    print("Duration in seconds:", duration.total_seconds())

    print()

    # 4.2
    dog = Mammal(
        "Buddy",
        5,
        18.5,
        "brown",
        4
    )

    eagle = Bird(
        "Eagle",
        8,
        5.2,
        2.1,
        True
    )

    snake = Reptile(
        "Python",
        3,
        7.0,
        "smooth",
        True
    )

    print("4.2 Applying Inheritance")

    print("Mammal:", dog.name)
    print("Fur color:", dog.fur_color)
    print("Number of legs:", dog.number_of_legs)
    dog.eat()
    dog.sleep()

    print()

    print("Bird:", eagle.name)
    print("Wingspan:", eagle.wingspan)
    print("Ability to fly:", eagle.ability_to_fly)
    eagle.eat()
    eagle.sleep()

    print()

    print("Reptile:", snake.name)
    print("Scale type:", snake.scale_type)
    print("Cold-bloodedness:", snake.cold_bloodedness)
    snake.eat()
    snake.sleep()
