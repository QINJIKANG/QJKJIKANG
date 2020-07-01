"""
老师接口
"""

from db import models


# 查看教授的课程
def check_teach_course_interface(tea_name):
    tea_obj = models.Teacher.select(tea_name)
    course_list = tea_obj.check_teach_course()

    if not course_list:
        return False, '您目前没有教授的课程！！'

    return True, course_list


# 选择课程
def choice_teach_course_interface(course_name, tea_name):
    tea_obj = models.Teacher.select(tea_name)
    course_list = tea_obj.teach_course_list

    if course_name in course_list:
        return False, '该课程您已选择过了！！'

    tea_obj.choice_teach_course(course_name)
    return True, f'课程：{course_name}选择成功！'


# 查看课程下的学生
def check_student_interface(course_name, tea_name):
    tea_obj = models.Teacher.select(tea_name)
    stu_list = tea_obj.check_student(course_name)

    if not stu_list:
        return False, '该课程下没有学生！！'

    return True, stu_list


# 修改分数
def change_score_interface(course_name, stu_name, score, tea_name):
    tea_obj = models.Teacher.select(tea_name)
    tea_obj.change_score(course_name, stu_name, score)
    return True, '修改成功！'

