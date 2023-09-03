from sqlalchemy import Column, Integer, String, ForeignKey, Table, Date
from sqlalchemy.orm import relationship, declarative_base, Mapped
import datetime


Base = declarative_base()

class FullName():
    fullname = Column(String, nullable=False)


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True) 
    group_name = Column(String(250), nullable=False)


class Student(Base, FullName):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True) 
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship(Group, backref='students')   


class Teacher(Base, FullName):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(250), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teachers: Mapped[list[Teacher]] = relationship(Teacher, backref='subjects')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    date = Column(Date, default=datetime.date.ctime)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship(Student, backref='grades')

    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship(Subject, backref='grades')
