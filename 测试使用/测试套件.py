from Lid.BeautifulReport3 import BeautifulReport
import operator
import unittest
test_suite = unittest.defaultTestLoader.discover('../Test_Case', pattern='test*.py')
report_file = BeautifulReport(test_suite).output_report()
print(report_file)



