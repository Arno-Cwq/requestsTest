#前后置
#直接在方法处把conn_qianhouzhi前后置方法当作参数写入方法即可实现前后置
import pytest
#作用于方法中的前后置
from common.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def conn_qianhouzhi():
    print("前置")
    yield
    print("后置")

#清除extract.yml文件
@pytest.fixture(scope="session",autouse=True)
def clean_yaml():
    YamlUtil().clean_extract_yaml()