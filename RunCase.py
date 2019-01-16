import shutil
import unittest
from threading import Thread
from HTMLTestReportCN import HTMLTestRunner
import time
import os


path = os.path.dirname(os.path.realpath(__file__))
Report_path = os.path.join(path, 'Report')

# 如果没有Report目录，创建
if not os.path.exists(Report_path):
    os.mkdir(Report_path)

files_count = len(os.listdir(Report_path))
if files_count > 10:
    # 如果report数量大于10条，清空目录
    shutil.rmtree(Report_path)
    os.mkdir(Report_path)


if __name__ == '__main__':
    case_path = './scripts/'
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_create_meeting_room.py')
    # 报告生成路径
    # Report/路径必须提前创建，否则报错
    report_path = './Report/'
    # 获取当前时间
    now_time = time.strftime('%Y-%m-%d %H-%M-%S')
    # 设置报告名称
    report_name = report_path + now_time + '-Report.html'
    # 打开并写入报告
    with open(report_name, 'wb') as f:
        # 初始化报告生成对象
        runner = HTMLTestRunner(stream=f, verbosity=2, title='Android自动化测试', description='UI自动化测试脚本', tester='Mr.Zhai')
        f = Thread(target=runner.run, args=(discover,))
        f.setDaemon(True)
        f.start()
