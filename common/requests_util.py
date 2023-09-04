#统一封装请求接口
import json

import requests
class RequestsUtil():
    #累变量、通过类名访问
    session = requests.session()
    def send_requests(self,method,url,data,**kwargs):
        rep = None
        if method =='get':
            rep = RequestsUtil.session.request(method,url = url,params = data,**kwargs)
        else:
            data = json.dumps(data)
            rep = RequestsUtil.session.request(method,url = url,data = data,**kwargs)
        return rep.text
