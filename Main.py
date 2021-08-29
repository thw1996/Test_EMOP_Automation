import allure
import pytest
import os
"""
allure 下载地址
https://github.com/allure-framework/allure2/releases
allure serve Report
"""
Report = os.path.join(os.path.dirname(os.path.abspath(__file__)),'Report')
if not os.path.exists(Report):
    os.mkdir(Report)


if __name__ == '__main__':
    # pytest.main(['-s', 'v', '--alluredir=%allure_result_folder%', './Report/xml'])
    pytest.main(['Test_Case','-s', '-v', f'--alluredir={Report}'])
    # print(Report)
    # pytest.main([ '-s', 'Test_Case','--alluredir','./Report'])
    # os.system("allure serve Report")