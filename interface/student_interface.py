"""
学生接口
"""
from db import models


# 注册接口
def register_interface(name, pwd):
    student_obj = models.Student.select(name)
    if student_obj:
        return False, '该用户名已存在！'

    student_obj = models.Student(name, pwd)
    student_obj.save()

    return True, f'学生{name}注册成功！'


# 选择学校接口
def choice_school_interface(school_name, student_name):
    stu_obj = models.Student.select(student_name)
    if stu_obj.school:
        return False, '您已经选择了学校！！'

    stu_obj.choice_school(school_name)
    return True, f'选择学校：{school_name}成功！'


# 查看当前学校课程
def check_course_interface(stu_name):
    stu_obj = models.Student.select(stu_name)
    school_name = stu_obj.school
    if not school_name:
        return False, '请先选择学校！'

    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list

    if not course_list:
        return False, '该校区没有课程！！'

    return True, course_list


# 选择课程
def choice_course_interface(course_name, student_name):
    stu_obj = models.Student.select(student_name)
    course_list = stu_obj.course_list
    if course_name in course_list:
        return False, '该课程已被选择！'

    stu_obj.choice_course(course_name)
    return True, f'课程：{course_name}选择成功！'


# 查看分数
def check_score_interface(stu_name):
    stu_obj = models.Student.select(stu_name)
    course_score = stu_obj.course_score
    if not course_score:
        return False, '暂时没有分数！'
    return True, course_score
