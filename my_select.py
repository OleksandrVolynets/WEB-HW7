from src.connect_db import session
from src.models import Grade, Group, Student, Subject, Teacher
from sqlalchemy import func, desc, select


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
def select_1():
    result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade_all_subjects')).select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade_all_subjects')).limit(5).all()

    return result

# Знайти студента із найвищим середнім балом з певного предмета.
def select_2(subject_name: str):
    result = session.query(Subject.subject_name, Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade).join(Student).join(Subject).filter(Subject.subject_name==subject_name).group_by(Student.id, Subject.subject_name).order_by(desc('avg_grade')).limit(1).all()

    return result

# Знайти середній бал у групах з певного предмета.
def select_3(subject_name: str):
    result = session.query(Subject.subject_name, Group.group_name, func.round(func.avg(Grade.grade), 2).label('avg_grade_by_subject')).select_from(Grade).join(Student).join(Group).join(Subject).filter(Subject.subject_name==subject_name).group_by(Group.group_name, Subject.subject_name).all()

    return result

# Знайти середній бал на потоці (по всій таблиці оцінок).
def select_4():
    result = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade_for_all_stream')).select_from(Grade).all()

    return result

# Знайти, які курси читає певний викладач.
def select_5(teacher_id: int):
    result = session.query(Teacher.fullname, Subject.subject_name).select_from(Subject).join(Teacher).filter(Teacher.id==teacher_id).all()
    return result

# Знайти список студентів у певній групі.
def select_6(group_id: int):
    result = session.query(Group.group_name, Student.fullname).select_from(Student).join(Group).filter(Group.id==group_id).all()
    return result

# Знайти оцінки студентів в окремій групі з певного предмета.
def select_7(group_id: int, subject: str):
    result = session.query(Group.group_name, Subject.subject_name, Student.fullname, Grade.grade).select_from(Grade).join(Subject).join(Student).join(Group).filter(Group.id==group_id).filter(Subject.subject_name==subject).all()
    return result

# Знайти середній бал, який ставить певний викладач зі своїх предметів.
def select_8(teacher_id: int):
    result = session.query(Teacher.fullname, Subject.subject_name, func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade).join(Subject).join(Teacher).filter(Teacher.id==teacher_id).group_by(Teacher.fullname, Subject.subject_name).all()
    return result

# Знайти список курсів, які відвідує певний студент.
def select_9(student_id: int):
    result = session.query(Student.fullname, Subject.subject_name).select_from(Grade).join(Student).join(Subject).filter(Student.id==student_id).all()
    return result
    
# Список курсів, які певному студенту читає певний викладач.
def select_10(student_id: int, teacher_id: int):
    result = session.query(Student.fullname, Teacher.fullname, Subject.subject_name).select_from(Grade).join(Subject).join(Teacher).join(Student).filter(Student.id==student_id).filter(Teacher.id==teacher_id).distinct().all()
    return result


if __name__ == '__main__':
    print(select_10(32, 1))
