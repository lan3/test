import json
import unittest

from TestingFramework.RequestMethod import send_requests


class TestDemo(unittest.TestCase):
    headers = None

    @classmethod
    def setUpClass(cls):
        # 设置请求头
        TestDemo.headers = {"Content-Type": "application/json;charset=UTF-8",
                            "Authorization": "eyJhbGciOiJIUzI1NiIsInppcCI6IkRFRiJ9.eNqqVnL28fTzdPZ0UbJSMjQwMDQAEUo6SqGhYCEjIDOzuBjIKkktLtErzs3MSS1JTS3J0EvOA0qlVhQoWRmamZpamBkZG5rqKOUlpUEEzC0NgAK1AAAAAP__.bszT9093tYDjnFMsbStuQVkNVLu43olFIb0fyd8LBDw",
                            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

    # 查询接口:get请求，无参数
    def test_01_selectDataAllByGet(self):
        response = send_requests('GET', 'https://test.smileteeth.cn/dmsapi/job/all/list', None, TestDemo.headers)
        print("test_01_selectDataAllByGet: ", response.text)

    # 查询接口:get请求，有参数
    def test_02_selectDataByGetAndParams(self):
        params = {
            "page": "1",
            "size": "10",
            "keywords": "蓝"
        }
        response = send_requests('GET', 'https://test.smileteeth.cn/dmsapi/account/list',
                                 params, TestDemo.headers)
        print("test_02_selectDataByGetAndParams: ", response.text)

    # 查询接口:post请求，无参数
    def test_03_selectDataAllByPost(self):
        response = send_requests('POST', 'https://test.smileteeth.cn/dmsapi/job/all/list', None, TestDemo.headers)
        print("test_03_selectDataAllByPost: ", response.text)

    # 查询接口:post请求，有参数
    def test_04_selectDataByPostAndParams(self):
        params = {
            "page": "1",
            "size": "10",
            "keywords": "李"
        }
        response = send_requests('GET', 'https://test.smileteeth.cn/dmsapi/account/list',
                                 params, TestDemo.headers)
        print("test_04_selectDataByPostAndParams: ", response.text)

    # 添加接口:post请求，有参数
    def test_05_addDataByPostAndParams(self):
        params = {
            "activeStatus": "0",
            "employeeID": "",
            "employeeName": "哈哈哈",
            "employeePhone": "13603065196",
            "jobType": "1",
            "roleID": "2",
            "userTags": "[{\"name\":\"认真\",\"type\":\"\"},{\"name\":\"勤劳\",\"type\":\"\"},{\"name\":\"敬业\","
                        "\"type\":\"\"}] "

        }
        response = send_requests('POST', 'https://test.smileteeth.cn/dmsapi/account/add',
                                 params, TestDemo.headers)
        print("test_05_addDataByPostAndParams: ", response.text)

    # 修改接口:post请求，有参数
    def test_06_updateDataByPostAndParams(self):
        params = {
            "activeStatus": "0",
            "employeeID": "22",
            "employeeName": "员工2",
            "employeePhone": "13603065196",
            "jobType": "2",
            "roleID": "1",
            "userTags": "[{\"name\":\"认真\",\"type\":\"\"},{\"name\":\"勤劳\",\"type\":\"\"},{\"name\":\"敬业\","
                        "\"type\":\"\"}] "

        }
        response = send_requests('POST', 'https://test.smileteeth.cn/dmsapi/account/update',
                                 params, TestDemo.headers)
        print("test_06_updateDataByPostAndParams: ", response.text)

    # 删除接口:post请求，有参数
    def test_07_deleteDataByPostAndParams(self):
        params = {
            "employeeID": "23"

        }

        response = send_requests('POST', 'https://test.smileteeth.cn/dmsapi/account/delete',
                                 params, TestDemo.headers)
        print("test_07_deleteDataByPostAndParams: ", response.text)

    if __name__ == '__main__':
        # 执行所有用例
        unittest.main()
