import os
import yaml


class YamlUtil:
    #读取yaml文件
    def read_extract_yaml(self):
        with open(os.getcwd()+"/extract.yml",mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value;

    #写入extract.yml文件
    def write_extract_yaml(self,data):
        with open(os.getcwd()+"/extract.yml",mode='w',encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode = True)

    # 清除extract.yml文件
    def clean_extract_yaml(self):
        with open(os.getcwd()+"/extract.yml", mode='w', encoding='utf-8') as f:
            #清除方法
            f.truncate()

    #读取测试用例的yml文件
    def read_testcase_yaml(self,yaml_name):
        with open(os.getcwd()+"./testcases/"+yaml_name, mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value;