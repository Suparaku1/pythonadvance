class Duration:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def get_minutes(self):
        return self.get_seconds() / 60.0

    def get_hours(self):
        return self.get_seconds() / 3600.0

    def print(self):
        print(f"Duration: {self.hours} hours, {self.minutes} minutes and {self.seconds} seconds")


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add(self, duration):
        # Convert both the current time and the duration into seconds.
        # This automatically handles overflow such as 75 seconds -> 1 minute 15 seconds.
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds += duration.get_seconds()

        # Convert the result back into hours, minutes and seconds.
        self.hours = total_seconds // 3600
        remainder = total_seconds % 3600
        self.minutes = remainder // 60
        self.seconds = remainder % 60

    def print(self):
        print(f"Time: {self.hours}:{self.minutes:02d}.{self.seconds:02d}")


# Example from the exercise:
d1 = Duration(1, 32, 45)
d1.print()
print(d1.get_seconds())
print(d1.get_hours())

t1 = Time(10, 52, 30)
t1.print()
t1.add(d1)
t1.print()
