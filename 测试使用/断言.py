import unittest
import logging
import re
class Ass(unittest.TestCase):
    def ass1(self):
        production =[2+4,22+4,("python"),100]
        test = [6,6,("python"),101]
        i = 0
        for p, t in zip(production, test):
            i = i+1
            try:
                self.assertEqual(p,t)
            except AssertionError as e:
                logging.info("断言失败")
                print("第{}个数据,数据对比失败:{}".format(i,e))
            else:
                logging.info("断言成功")
                print("第{}个数据,数据对比成功".format(i))





class Duibi(unittest.TestCase):
    # 话术对较
    # production = production['result']
    # test = test['result']
    def duibi(self):
        production = [{"step":"4"},{"talkContent":"5"},{"ordernum":"6"},{"isRead":"7"}]
        test = [{"step":"4"},{"talkContent":"5"},{"ordernum":"8"},{"isRead":"7"}]
        production1 = ["step","talkContent","ordernum","isRead"]
        production = list(production)
        test = list(test)
        i = 0
        for p,t,j in zip(production,test,production1):
            i = i + 1
            try:
                self.assertEqual(p[j],t[j])
            except AssertionError as e:
                f = re.sub(r'\n.*.','',str(e))
                e = re.sub(r'\n','',f)
                logging.info("断言失败")
                print("第{}个数据,数据对比失败:{}".format(i, e))
            else:
                logging.info("断言成功")
                print("第{}个数据,数据对比成功".format(i))

if __name__ == '__main__':
    # Ass().ass1()
    Duibi().duibi()
