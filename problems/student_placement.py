#!/usr/bin/env python3
import random

"""
Given a list of schools, a list of students with choices of schools, and capacity for
each school, print out each school with students placed
"""

NUM_SCHOOLS      = 5
DEFAULT_CAPACITY = 5
NUM_STUDENTS     = 10

class School:
    def __init__(self, name, capacity):
        self.name = name
        self.students = []
        self.capacity = capacity

    def at_capacity(self):
        return self.capacity == len(self.students)

    def print_students(self):
        for student in self.students:
            student.print_choices()

class Student:
    def __init__(self, choices, schools_available):
        self.schools = []
        for choice in choices:
            self.schools.append(schools_available[choice])
        self.placed = False

    def print_choices(self):
        s = []
        for school in self.schools:
            s.append(school.name)
        print('Student: [{}]'.format(', '.join(s)))

def main():
    # generate arguments
    capacity = DEFAULT_CAPACITY
    schools = []
    for i in range(NUM_SCHOOLS):
        school_name = '%s' % i
        schools.append(School(school_name, capacity))
    students = [Student([0,1,2,3,4], schools) for _ in range(14)]
    students.extend([Student([4,3,2,1,0], schools) for _ in range(3)])
    students.append(Student([2,1,4,3,0], schools))
    students.extend([Student([3,4,0,1,2], schools) for _ in range(7)])
    round_based(schools, students)

def round_based(schools, students):
    assert(len(students) <= (len(schools) * schools[0].capacity))
    random.SystemRandom().shuffle(students)

    # outer loop index of choice, inner loop students
    # assume each school has same capacity
    for i in range(schools[0].capacity):
        for student in students:
            if student.placed:
                continue
            school = student.schools[i]
            if not school.at_capacity():
                school.students.append(student)
                student.placed = True
    print_final_school_placements(schools)

def print_final_school_placements(schools):
    for school in schools:
        print(school.name)
        school.print_students()
        print()

if __name__ == '__main__':
    main()