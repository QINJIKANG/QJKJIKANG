"""
管理员视图

1、管理员功能
-  登录
-  注册
- 创建学校
- 创建课程
- 创建老师
"""

from interface import admin_interface, common_interface
from lib import common

admin_name = {'user': None}


# 登录
def login():
    while 1:
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()

        flag, msg = common_interface.login_interface(
            name, pwd, 'admin'
        )
        if flag:
            print(msg)
            admin_name['user'] = name
            break

        else:
            print(msg)


# 注册
def register():
    while 1:
        name = input('请输入注册用户名：').strip()
        pwd = input('请输入注册密码：').strip()
        re_pwd = input('请核实注册密码：').strip()

        if pwd != re_pwd:
            print('两次密码不一致！')
            continue

        flag, msg = admin_interface.register_interface(
            name, pwd
        )
        if flag:
            print(msg)
            break

        else:
            print(msg)


# 创建学校
@common.auth('admin')
def create_school():
    while 1:
        school_name = input('请输入学校的名字：').strip()

        flag, msg = admin_interface.create_school_interface(
            school_name, admin_name.get('user')
        )
        if flag:
            print(msg)
            break

        else:
            print(msg)


# 创建课程
@common.auth('admin')
def create_course():
    while 1:
        flag, msg = common_interface.check_all_school_interface()
        if not flag:
            print(msg)
            break

        for index, school_name in enumerate(msg):
            print(f'编号：{index}  校名：{school_name}')

        cmd = input('请选择编号：').strip()

        if not cmd.isdigit():
            print('请输入数字！！')
            continue

        cmd = int(cmd)

        if cmd not in range(len(msg)):
            print('请输入正确的编号！！')
            continue

        school_name = msg[cmd]

        course_name = input('请输入课程名：').strip()

        flag1, msg1 = admin_interface.create_course_interface(
            school_name, course_name, admin_name.get('user')
        )
        if flag1:
            print(msg1)
            break

        else:
            print(msg1)


# 创建老师
@common.auth('admin')
def create_teacher():
    while 1:
        name = input('请输入老师的姓名：').strip()
        flag, msg = admin_interface.create_teacher_interface(name, admin_name.get('user'))

        if flag:
            print(msg)
            break


func_dic = {
    '1': login,
    '2': register,
    '3': create_school,
    '4': create_course,
    '5': create_teacher
}


def run():
    while 1:
        print('''
        ==== 管理员系统 ====
           1 登录
           2 注册
           3 创建学校
           4 创建课程
           5 创建老师
        =================
        ''')

        cmd = input('请输入命令编号(按q退出)>>>').strip()

        if cmd == 'q':
            break

        if cmd not in func_dic:
            print('请输入正确的指令！！')
            continue

        func_dic[cmd]()
