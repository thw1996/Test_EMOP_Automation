import unittest
from Lid.logger import Log


class TestAdd(unittest.TestCase):
    print("这是ccc")
    Log().info("这是ccc")

    def testadd(self):
        """测试打印aaa"""
        print("这是aaa")
        Log().info("这是aaa")

    def testbdd(self):
        """测试打印bbb"""
        print("这是bbb")
        Log().info("这是bbb")




if __name__ == '__main__':
    TestAdd().testadd()
    TestAdd().testbdd()








