"""
    使用DDT数据驱动

"""
import unittest

import ddt


@ddt.ddt
class TestHttpDDT(unittest.TestCase):
    guests = ({'value1': '孙俪', 'value2': '邓超'},

              {'value1': '蔡少芬', 'value2': '张晋'},

              {'value1': '袁咏仪', 'value2': '张智霖'})

    # 数据是单个值
    @ddt.data(1, 2, 3)
    def test_01(self, value):
        print("tuple:", value)

    # 数据是元组
    @ddt.unpack
    @ddt.data((1, 11), (2, 22), (3, 33))
    def test_02(self, value1, value2):
        print("tuple1:", value1, "tuple2:", value2)

    # 数据是列表
    @ddt.unpack
    @ddt.data([1, 11], [2, 22], [3, 33])
    def test_03(self, value1, value2):
        print("list1:", value1, "list2:", value2)

    # 数据是字典
    @ddt.unpack
    @ddt.data({'value1': '孙俪', 'value2': '邓超'},

              {'value1': '蔡少芬', 'value2': '张晋'},

              {'value1': '袁咏仪', 'value2': '张智霖'})
    def test_04(self, value1, value2):
        print("dict1:", value1, "dict2", value2)

    # 数据先定义
    @ddt.data(*guests)
    def test_05(self, guests):
        print("女嘉宾是", guests['value1'], "男嘉宾是", guests['value2'])

    # 将json文件注入测试用例中:取值方法一
    @ddt.file_data('Parameters.json')
    def test_06(self, userName, passWord):
        print("姓名：", userName, "密码：", passWord)

    # 将json文件注入测试用例中：取值方法二
    @ddt.file_data('Parameters.json')
    def test_07(self, **data):
        print("data:", data)
        print("姓名2：", data['userName'], "密码2：", data['passWord'])


if __name__ == '__main__':
    unittest.main()
