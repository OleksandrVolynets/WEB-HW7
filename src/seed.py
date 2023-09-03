from connect_db import session
from models import Grade, Group, Student, Subject, Teacher
from datetime import date
from faker import Faker
from random import randint


GRADES_MAX_QTY = 20
GROUPS_QTY = 3
STUDENTS_QTY = 50
SUBJECTS_QTY = 6
TEACHERS_QTY = 5


fake = Faker('UK-UA')

def random_symbol():
    return chr(randint(ord('A'), ord('Z')))


def create_fake_data(groups_qty, students_qty, teachers_qty):

    fake_groups = list()
    fake_students = list()
    fake_subjects = ['Physics', 'Math', 'Biology', 'Geology', 'Chemistry', 'Drilling']
    fake_teachers = list()

    for _ in range(groups_qty):
        group = str()
        while len(group) < 5:
            group += random_symbol()
        group += '-2023'
        fake_groups.append(group)
        group = []

    for _ in range(students_qty):
        fake_students.append(fake.name())

    for _ in range(teachers_qty):
        fake_teachers.append(fake.name())    

    return fake_groups, fake_students, fake_subjects, fake_teachers


def fill_data(groups, students, subjects, teachers):

    for group in groups:
        session.add(Group(group_name=group))

    for student in students:
        session.add(Student(fullname=student, group_id=randint(1, GROUPS_QTY)))

    for subject in subjects:
        session.add(Subject(subject_name=subject, teacher_id=randint(1, TEACHERS_QTY)))

    for teacher in teachers:
        session.add(Teacher(fullname=teacher, ))

    for student_id in range(1, STUDENTS_QTY+1):
        i = 1
        while i <= randint(1, GRADES_MAX_QTY):
            session.add(Grade(grade=randint(1, 12), date=fake.date_between_dates(date(2023,1,1), date(2023,9,1)), student_id=student_id, subject_id=randint(1, SUBJECTS_QTY)))
            i += 1

    session.commit()


def run():
    fill_data(*create_fake_data(GROUPS_QTY, STUDENTS_QTY, TEACHERS_QTY))


if __name__ == "__main__":
    run()    


