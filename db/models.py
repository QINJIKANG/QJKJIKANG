"""
存放类
"""
from db import db_handler


# 父类
class Base:

    def save(self):
        db_handler.save_info(self)

    @classmethod
    def select(cls, name):
        obj = db_handler.select_info(cls, name)
        return obj


# 管理员类
class Admin(Base):

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd

    def create_school(self, school_name):
        school_obj = School(school_name)
        school_obj.save()

    def create_course(self, school_obj, course_name):
        course_obj = Course(course_name)
        course_obj.save()
        school_obj.course_list.append(course_name)
        school_obj.save()

    def create_teacher(self, name, pwd):
        tea_obj = Teacher(name, pwd)
        tea_obj.save()


# 学校类
class School(Base):

    def __init__(self, name):
        self.name = name
        self.course_list = []


# 学生类
class Student(Base):

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.course_score = {}

    def choice_school(self, school_name):
        self.school = school_name
        self.save()

    def choice_course(self, course_name):
        self.course_list.append(course_name)
        self.course_score[course_name] = 0
        self.save()
        course_obj = Course(course_name)
        course_obj.student_list.append(self.name)
        course_obj.save()


# 课程类
class Course(Base):

    def __init__(self, name):
        self.name = name
        self.student_list = []


# 老师类
class Teacher(Base):

    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.teach_course_list = []

    def check_teach_course(self):
        return self.teach_course_list

    def choice_teach_course(self, course_name):
        self.teach_course_list.append(course_name)
        self.save()

    def check_student(self, course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    def change_score(self, course_name, stu_name, score):
        stu_obj = Student.select(stu_name)
        stu_obj.course_score[course_name] = score
        stu_obj.save()
