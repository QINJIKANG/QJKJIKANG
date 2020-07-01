"""
公共接口
"""
import os
from conf import settings
from db import models


# 登录接口
def login_interface(name, pwd, types):
    if types == 'admin':
        obj = models.Admin.select(name)

    elif types == 'student':
        obj = models.Student.select(name)

    elif types == 'teacher':
        obj = models.Teacher.select(name)

    else:
        return False, '角色不存在！'

    if obj:
        if pwd == obj.pwd:
            return True, f'{name}登录成功！'
        return False, '密码错误！'
    return False, '用户不存在！'


# 查看所有的校区接口
def check_all_school_interface():
    school_dir = os.path.join(settings.DB_PATH, 'School')

    if not os.path.exists(school_dir):
        return False, '暂时没有校区，请联系管理员'

    school_list = os.listdir(school_dir)
    return True, school_list


# 查看学校下的课程
def check_all_course_interface(school_name):
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if not course_list:
        return False, '该学校还没有课程！！'

    return True, course_list
