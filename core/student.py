"""
学生视图

2、学生功能
-  登录
-  注册
- 选择学校
- 选择课程
- 查看分数
"""
from interface import student_interface, common_interface
from lib import common
student_name = {'user': None}


# 登录
def login():
    while 1:
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()

        flag, msg = common_interface.login_interface(
            name, pwd, 'student'
        )
        if flag:
            print(msg)
            student_name['user'] = name
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

        flag, msg = student_interface.register_interface(
            name, pwd
        )
        if flag:
            print(msg)
            break

        else:
            print(msg)


# 选择学校
@common.auth('student')
def choice_school():
    while 1:
        flag, msg = common_interface.check_all_school_interface()
        if not flag:
            print(msg)
            break

        for index, school_name in enumerate(msg):
            print(f'编号：{index}  校名：{school_name}')

        cmd = input('请选择学校编号：').strip()

        if not cmd.isdigit():
            print('请输入数字！！')
            continue

        cmd = int(cmd)

        if cmd not in range(len(msg)):
            print('请输入正确的编号！！')
            continue

        school_name = msg[cmd]

        flag1, msg1 = student_interface.choice_school_interface(
            school_name, student_name.get('user')
        )
        if flag1:
            print(msg1)
            break

        else:
            print(msg1)



# 选择课程
@common.auth('student')
def choice_course():
    while 1:
        flag, msg = student_interface.check_course_interface(
            student_name.get('user')
        )
        if not flag:
            print(msg)
            break

        for index, course_name in enumerate(msg):
            print(f'编号：{index}  课程名：{course_name}')

        cmd = input('请选择课程编号：').strip()

        if not cmd.isdigit():
            print('请输入数字！！')
            continue

        cmd = int(cmd)

        if cmd not in range(len(msg)):
            print('请输入正确的编号！！')
            continue

        course_name = msg[cmd]

        flag1, msg1 = student_interface.choice_course_interface(
            course_name, student_name.get('user')
        )
        if flag1:
            print(msg1)
            break

        else:
            print(msg1)


# 查看分数
@common.auth('student')
def check_score():
    flag, msg = student_interface.check_score_interface(
        student_name.get('user')
    )
    if flag:
        print(msg)

    else:
        print(msg)


func_dic = {
    '1': login,
    '2': register,
    '3': choice_school,
    '4': choice_course,
    '5': check_score}


def run():
    while 1:
        print('''
        ==== 学生系统 ====
             1 登录
             2 注册
             3 选择学校
             4 选择课程
             5 查看分数
        =================
        ''')

        cmd = input('请输入命令编号(按q退出)>>>').strip()

        if cmd == 'q':
            break

        if cmd not in func_dic:
            print('请输入正确的指令！！')
            continue

        func_dic[cmd]()
