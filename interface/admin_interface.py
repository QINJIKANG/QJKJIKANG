"""
管理员接口
"""
from db import models


# 注册接口
def register_interface(name, pwd):
    admin_obj = models.Admin.select(name)
    if admin_obj:
        return False, '该用户名已存在！'

    admin_obj = models.Admin(name, pwd)
    admin_obj.save()

    return True, f'管理员{name}注册成功！'


# 创建学校接口
def create_school_interface(school_name, admin_name):
    admin_obj = models.Admin.select(admin_name)
    school_obj = models.School.select(school_name)

    if school_obj:
        return False, '该学校已存在！'

    admin_obj.create_school(school_name)
    return True, f'学校：{school_name}创建成功！'


# 创建课程接口
def create_course_interface(school_name, course_name, admin_name):
    school_obj = models.School.select(school_name)
    if course_name in school_obj.course_list:
        return False, '该课程已存在！'

    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_obj, course_name)

    return True, f'课程：{course_name}创建成功！'


# 创建老师接口
def create_teacher_interface(name, admin_name, pwd='666'):
    admin_obj = models.Admin.select(admin_name)
    tea_obj = models.Teacher.select(name)
    if tea_obj:
        return False, '该老师已创建！'

    admin_obj.create_teacher(name, pwd)
    return True, f'老师：{name}创建成功！'

