"""
老师视图

- 登录
- 查看教授课程
- 选择教授课程
- 查看课程下学生
- 修改分数
"""
from interface import teacher_interface, common_interface
from lib import common
teacher_name = {'user': None}


# 登录
def login():
    while 1:
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()

        flag, msg = common_interface.login_interface(
            name, pwd, 'teacher'
        )
        if flag:
            print(msg)
            teacher_name['user'] = name
            break

        else:
            print(msg)


# 查看教授课程
@common.auth('teacher')
def check_teach_course():
    flag, msg = teacher_interface.check_teach_course_interface(
        teacher_name.get('user')
    )
    if flag:
        print(msg)
    else:
        print(msg)


# 选择教授课程
@common.auth('teacher')
def choice_teach_course():
    while 1:
        flag, msg = common_interface.check_all_school_interface()
        if not flag:
            print(msg)
            break

        for index, school_name in enumerate(msg):
            print(f'编号：{index}  校名：{school_name}')

        cmd = input('请先选择学校编号：').strip()

        if not cmd.isdigit():
            print('请输入数字！！')
            continue

        cmd = int(cmd)

        if cmd not in range(len(msg)):
            print('请输入正确的编号！！')
            continue

        school_name = msg[cmd]

        flag1, msg1 = common_interface.check_all_course_interface(
            school_name
        )
        if not flag1:
            print(msg1)


        for index1, course_name in enumerate(msg1):
            print(f'编号：{index1} 课程名：{course_name}')

        cmd1 = input('请选择课程编号：').strip()

        if not cmd1.isdigit():
            print('请输入数字！！')
            continue

        cmd1 = int(cmd1)

        if cmd1 not in range(len(msg1)):
            print('请输入正确的编号！！')
            continue

        course_name = msg1[cmd1]

        flag2, msg2 = teacher_interface.choice_teach_course_interface(
            course_name, teacher_name.get('user')
        )
        if flag2:
            print(msg2)
            break

        else:
            print(msg2)



# 查看课程下学生
@common.auth('teacher')
def check_teach_student():
    while 1:
        flag, msg = teacher_interface.check_teach_course_interface(
            teacher_name.get('user')
        )
        if not flag:
            print(msg)
            break

        for index, course_name in enumerate(msg):
            print(f'编号：{index} 课程名：{course_name}')

        cmd = input('请选择课程编号：').strip()

        if not cmd.isdigit():
            print('请输入数字！！')
            continue

        cmd = int(cmd)

        if cmd not in range(len(msg)):
            print('请输入正确的编号！！')
            continue

        course_name = msg[cmd]

        flag1, msg1 = teacher_interface.check_student_interface(
            course_name, teacher_name.get('user')
        )
        if flag1:
            print(msg1)
            break
        else:
            print(msg1)



# 修改分数
@common.auth('teacher')
def change_score():
    while 1:
        flag, msg = teacher_interface.check_teach_course_interface(
            teacher_name.get('user')
        )
        if not flag:
            print(msg)
            break

        for index, course_name in enumerate(msg):
            print(f'编号：{index} 课程名：{course_name}')

        cmd = input('请选择课程编号：').strip()

        if not cmd.isdigit():
            print('请输入数字！！')
            continue

        cmd = int(cmd)

        if cmd not in range(len(msg)):
            print('请输入正确的编号！！')
            continue

        course_name = msg[cmd]

        flag1, msg1 = teacher_interface.check_student_interface(
            course_name, teacher_name.get('user')
        )
        if not flag1:
            print(msg1)
            break

        for index1, stu_name in enumerate(msg1):
            print(f'编号：{index1} 学生名：{stu_name}')

        cmd1 = input('请选择学生编号：').strip()

        if not cmd1.isdigit():
            print('请输入数字！')
            continue

        cmd1 = int(cmd1)

        if cmd1 not in range(len(msg1)):
            print('请输入正确的编号！！')
            continue

        stu_name = msg1[cmd1]

        score = input('请输入分数：').strip()

        if not score.isdigit():
            print('请输入数字！')
            continue

        score = int(score)

        flag2, msg2 = teacher_interface.change_score_interface(
            course_name, stu_name, score, teacher_name.get('user')
        )
        if flag2:
            print(msg2)
            break


func_dic = {
    '1': login,
    '2': check_teach_course,
    '3': choice_teach_course,
    '4': check_teach_student,
    '5': change_score}


def run():
    while 1:
        print('''
        ==== 学生系统 ====
          1 登录
          2 查看教授课程
          3 选择教授课程
          4 查看课程下学生
          5 修改分数
        =================
        ''')

        cmd = input('请输入命令编号(按q退出)>>>').strip()

        if cmd == 'q':
            break

        if cmd not in func_dic:
            print('请输入正确的指令！！')
            continue

        func_dic[cmd]()
