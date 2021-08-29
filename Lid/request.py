import requests
from Lid.logger import Log
import json

class Request:
    def cookie(self,method,url1,loging_data1):
        Log().infp("请求方式:{},url{},请求体:{}".format(method,url1,loging_data1))
        res = requests.request(method,url1,data=loging_data1,verify=False)
        Log().info("响应{}".format(res.json()))
        cookies = {"JSESSIONID":res.cookies["JSESSIONID"]}
        Log().info("cookie:{}".format(cookies))
        return cookies

    def request(self,method,url1,loging_data1,url,login_data):
        Log().infp("请求方式:{},url{},请求体:{}".format(method,url,login_data))
        cookie = self.cookie(method,url1,loging_data1)
        res = requests.request(method,url,json=login_data,cookies=cookie,verify=False)
        Log().info("响应{}".format(res.json()))
        return res

if __name__ == "__main__":
    login_data = {"userId":"004","password":"004"}
