import os
import unittest
from HTMLTestRunner import HTMLTestRunner
from utils.addPath import AddPath

class RunAllCase():

    @classmethod
    def setUpClass(cls):
        AddPath.add_project_path()


    @staticmethod
    def run_all():
        try:
            report_path =os.path.dirname(os.getcwd())
            file_apth = report_path + "/report/"
            if not os.path.exists(file_apth):
                os.mkdir(file_apth)
            file_name = file_apth + "result.html"

            test_model = "../cases/"

            discover = unittest.defaultTestLoader.discover(test_model,pattern="test*.py")
            with open(file_name,"wb")as f:
                runner =HTMLTestRunner(stream=f, verbosity=2, title="安卓自动化测试报告",description="测试用例运行详情")
                runner.run(discover)

        except Exception as e:
            print(e)
    @classmethod
    def tearDownClass(cls):
        print("测试结束")


if __name__ == '__main__':
    RunAllCase.setUpClass()
    RunAllCase.run_all()
    RunAllCase.tearDownClass()

