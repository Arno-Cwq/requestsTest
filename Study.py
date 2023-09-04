#设置name为全局变量
class Study():
    # test = ""
    # name = ""
    #参数写入
    # @pytest.mark.parametrize('name,age',[['陈伟强','13岁'],['陈大强','14岁'],['陈小强','15岁']])
    # def test_case01(self,name,age,conn_qianhouzhi):
        # url = "172.16.0.181:8508"
        # data = {
        #
        # }
        # rel = requests.get(url=url)
        # rep = name+age
        # print(rep)
        # #提取数据到全局变量
        # Test_case.name = rep
        # Test_case.test = re.search("陈小强(.*?)岁",rep)
    # def test_01(self):
    #     #运用全局变量
    #     print(Test_case.name)
    #     print(Test_case.test)
    def test(self):
        return None
        # url = "http://172.16.0.181:8508/pwrApi/infoscreen/pdeScreen/list"
        # data = {
        #     "projectId":"2c92808e80f408230180f4a9e28d04c8"
        # }
        # headers = {
        #     "userToken":"63a6ccdb684d00d55566ca7cba3b7836",
        #     "Content-Type":"application/json; charset=UTF-8"
        # }
        # rep02 = requests.get(url = url,params = data,headers = headers)
        # print(rep02.text)
        # 正则表达式提取,[1]表示获得的第一个值
        # Test_case.tiqu = re.search('"oid":"(.*?)"',rep02.text)[1]
        # print(Test_case.tiqu)
        # print("我是"+Test_case.tiqu+"的")
        # 断言
        # assert 'oid' in rep02.text
        # assert rep02.json()['data'][0]['oid'] == '1529659839184179202'
        # def test_03(self):
        #     print("oid是："+Test_case.tiqu)
        #     #读取yml文件的数据
        #     test001 = YamlUtil().read_extract_yaml()['oid']
        #     print(test001)