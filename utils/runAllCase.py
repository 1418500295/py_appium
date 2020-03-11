import os
import sys
import unittest
# from HTMLTestRunner import HTMLTestRunner
from BeautifulReport import BeautifulReport


class RunAllCase():

    @classmethod
    def setUpClass(cls):
        project_path = os.path.dirname(os.getcwd())
        sys.path.append(project_path)



    @staticmethod
    def run_all():
        try:
            """
            定义测试报告路径
            """
            project_path =os.path.dirname(os.getcwd())
            report_apth = project_path + "/report/"
            if not os.path.exists(report_apth):
                os.mkdir(report_apth)

            test_model = "../cases/"

            discover = unittest.defaultTestLoader.discover(test_model,pattern="test*.py")

            result = BeautifulReport(discover)
            # log_path为测试报告的生成路径
            result.report(filename="report",description="安卓自动化报告",log_path=report_apth)


        except Exception as e:
            print(e)
    @classmethod
    def tearDownClass(cls):
        print("测试结束")


if __name__ == '__main__':
    RunAllCase.setUpClass()
    RunAllCase.run_all()
    RunAllCase.tearDownClass()

