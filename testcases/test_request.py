#一个py文件可以对应N个接口
import json
import os
import re
import pytest
import requests
from common.requests_util import RequestsUtil
from common.yaml_util import YamlUtil
class Test_case():
    #读取yaml数据
    @pytest.mark.parametrize('duquyongli',YamlUtil().read_testcase_yaml('data.yml'))
    def test_02(self,conn_qianhouzhi,duquyongli):
        print(duquyongli['name'])
        print(duquyongli['request']['method'])
        print(duquyongli['request']['url'])
        print(duquyongli['request']['data'])
        print(duquyongli['request']['headers'])
        method = duquyongli['request']['method']
        url = duquyongli['request']['url']
        data = duquyongli['request']['data']
        headers = duquyongli['request']['headers']
        test = RequestsUtil().send_requests(method,url,data,headers = headers)
        result01 = json.loads(test)
        result02 = result01['code']
        print(test)
        # print(result02)
        print(result01)
        #断言处理
        if int(result02)>0:
            YamlUtil().write_extract_yaml({'oid':result01['code']})
            assert int(result02)>0
        else:
            print("异常用例")
        print(result02)
        #利用json提取将键值对写入yaml文件
        YamlUtil().write_extract_yaml({'oid':result02})
