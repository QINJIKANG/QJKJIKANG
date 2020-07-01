"""
公共功能
"""


# 认证装饰器
def auth(role):
    from core import admin, student, teacher

    def outer(func):
        def inner(*args, **kwargs):
            if role == 'admin':
                if admin.admin_name['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('请先登录！')
                    admin.login()

            if role == 'student':
                if student.student_name['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('请先登录！')
                    student.login()

            if role == 'teacher':
                if teacher.teacher_name['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('请先登录！')
                    teacher.login()

        return inner

    return outer
