import os
import yaml


class ReadYaml():

    @staticmethod
    def get_yaml(file_name):
        project_path = os.path.dirname(os.getcwd())
        print(project_path)
        target_file_name = project_path + "/" + file_name
        with open(target_file_name,"r",encoding="utf-8")as f:
            res_data = yaml.load(f,Loader=yaml.FullLoader)
            return res_data

if __name__ == '__main__':
    print(ReadYaml.get_yaml("app_config.yaml"))