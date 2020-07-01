"""
主程序
"""
from core import admin, student, teacher

func_dic = {
    '1': admin.run,
    '2': student.run,
    '3': teacher.run
}


def run():
    while 1:
        print('''
        ==== 选课系统 ====
            1 管理员入口
            2 学生入口
            3 老师入口
        =================
        ''')

        cmd = input('请输入命令编号(按q退出)>>>').strip()

        if cmd == 'q':
            break

        if cmd not in func_dic:
            print('请输入正确的指令！！')
            continue

        func_dic[cmd]()
