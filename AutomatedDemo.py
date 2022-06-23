import unittest
import json
import ddt
from TestingFramework.ConnectDatabase import connect_database, close_database, execute_sql
from TestingFramework.RequestMethod import send_requests


@ddt.ddt
class AutomatedDemo(unittest.TestCase):
    conn = None
    cursor = None
    headers = None

    @classmethod
    def setUpClass(cls):
        # 获得数据库连接
        AutomatedDemo.conn, AutomatedDemo.cursor = connect_database()
        # 设置请求头
        AutomatedDemo.headers = {"Content-Type": "application/json;charset=UTF-8",
                                 "Authorization": "eyJhbGciOiJIUzI1NiIsInppcCI6IkRFRiJ9.eNqqVnL28fTzdPZ0UbJSMjQwMDQAEUo6SqGhYCEjIDOzuBjIKkktLtErzs3MSS1JTS3J0EvOA0qlVhQoWRmamZpaGpsam5rrKOUlpUEELMyMgQK1AAAAAP__.Cbwx_IInab9V6QxP0Ec11IqDVgvTnDoh5V5ld4Z3LiU",
                                 "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}

    # 判断查询的数据是否正确
    def test_01(self):
        params = {
            "page": "1",
            "size": "10",
            "keywords": "李"
        }
        # 调用接口，获取接口返回值
        response = send_requests('GET', 'https://test.smileteeth.cn/dmsapi/account/list',
                                 params, AutomatedDemo.headers)
        response = json.loads(response.text)
        print("test_01 response:", response['data']['content'])
        # 执行SQL，获取数据库返回值
        result = execute_sql(AutomatedDemo.conn, AutomatedDemo.cursor, 'SELECT',
                             "SELECT * FROM `sys_employee` WHERE `EmployeeName` LIKE '%李%' ORDER BY `EmployeeID` DESC;")
        print("test_01 result:", result)
        self.respList = []
        self.resuList = []
        for resp in response['data']['content']:
            self.respList.append(resp['employeeID'])

        for resu in result:
            self.resuList.append(resu['EmployeeID'])
        # 判断接口返回的数据ID是否和sql返回的数据的ID一致
        self.assertEqual(self.respList, self.resuList, 'test_01 查询到的数据有误！')

    # 判断是否添加，修改或删除成功
    def test_02(self):
        params = {
            "activeStatus": "0",
            "employeeID": "",
            "employeeName": "哈哈哈5",
            "employeePhone": "13603065196",
            "jobType": "1",
            "roleID": "2",
            "userTags": "[{\"name\":\"认真\",\"type\":\"\"},{\"name\":\"勤劳\",\"type\":\"\"},{\"name\":\"敬业\","
                        "\"type\":\"\"}] "

        }
        # 调用接口，添加数据
        response = send_requests('POST', 'https://test.smileteeth.cn/dmsapi/account/add',
                                 params, AutomatedDemo.headers)
        response = json.loads(response.text)
        # 判断接口返回的code状态是否是000000
        self.assertEqual(response['code'], '000000', 'test_02 添加失败！失败原因：' + response['codeDesc'])

    # 判断查询的数据是否正确:数据驱动
    @ddt.file_data('Keywords.json')
    def test_03(self, **params):
        # 调用接口，获取接口返回值
        response = send_requests('GET', 'https://test.smileteeth.cn/dmsapi/account/list',
                                 params, AutomatedDemo.headers)
        response = json.loads(response.text)
        print("test_03 response:", response['data']['content'])
        # 执行SQL，获取数据库返回值
        result = execute_sql(AutomatedDemo.conn, AutomatedDemo.cursor, 'SELECT',
                             "SELECT * FROM `sys_employee` WHERE `EmployeeName` LIKE '%" + params[
                                 'keywords'] + "%' ORDER BY `EmployeeID` DESC;")
        print("test_03 result:", result)
        self.respList = []
        self.resuList = []
        for resp in response['data']['content']:
            self.respList.append(resp['employeeID'])

        for resu in result:
            self.resuList.append(resu['EmployeeID'])
        # 判断接口返回的数据ID是否和sql返回的数据的ID一致
        self.assertEqual(self.respList, self.resuList, 'test_03 查询到的数据有误！')

    @classmethod
    def tearDownClass(cls):
        # 关闭数据库连接
        close_database(AutomatedDemo.conn, AutomatedDemo.cursor)

    if __name__ == '__main__':
        testSuite = unittest.TestSuite
        suite = unittest.TestLoader().discover('.', 'AutomatedDemo.py')
        testSuite.addTests(suite)
        fp = open('./result.html', "wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="自动化测试unittest测试框架报告", description="用例执行情况：")
        runner.run(testSuite)
        fp.close()
