import os
import sys

class AddPath():

    @staticmethod
    def add_project_path():
        project_path = os.path.dirname(os.getcwd())
        sys.path.append(project_path)
