class Professor:
    def __init__(self, name):
        self.name = name
        self.courses = []


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

        if self not in course.students:
            course.students.append(self)


class Room:
    def __init__(self, number):
        self.number = number
        self.courses = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

        if course.room is not self:
            course.room = self


class Course:
    def __init__(self, name, professor):
        self.name = name
        self.professor = professor
        self.students = []
        self.room = None

        professor.courses.append(self)

    def assign_room(self, room):
        room.add_course(self)

    def __str__(self):
        return self.name


def validate_domain(professors, students, courses, rooms):
    for course in courses:
        if course.professor is None:
            raise ValueError(
                f"Course '{course.name}' must have exactly one professor."
            )

    for room in rooms:
        if len(room.courses) == 0:
            raise ValueError(
                f"Room '{room.number}' must be used by at least one course."
            )


# Create objects
professor = Professor("Stefan Hörmann")

student1 = Student("Esmerald")
student2 = Student("Anna")

course = Course(
    "Object-Oriented Programming",
    professor
)

room = Room("A101")

# Create associations
student1.add_course(course)
student2.add_course(course)

course.assign_room(room)

# Lists of all objects
professors = [professor]
students = [student1, student2]
courses = [course]
rooms = [room]

# Validate the domain model
validate_domain(
    professors,
    students,
    courses,
    rooms
)

# Output
print("Course:", course.name)
print("Professor:", course.professor.name)
print("Students:")

for student in course.students:
    print("-", student.name)

print("Room:", course.room.number)
