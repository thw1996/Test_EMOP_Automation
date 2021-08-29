from selenium import webdriver
driver = webdriver.Chrome()
import unittest
#高亮显示
def highlight(self, element):
    for i in range(150):
        if i % 2 == 0:
            driver.execute_script("arguments[0].style.border='4px solid red'", element)
        else:
            driver.execute_script("arguments[0].style.border=''", element)
#断言
class TestAssert(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(2+2,4)
        self.assertEqual(4,4)

if __name__ == '__main__':
    unittest.main()




driver.find_element()
driver.find_element_by_id()
driver.find_element_by_css_selector()
driver.find_element_by_class_name()
driver.find_element_by_xpath()
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()
driver.find_element_by_name()
driver.find_element_by_tag_name()

driver.find_elements()
driver.find_elements_by_class_name()
driver.find_elements_by_css_selector()
driver.find_elements_by_xpath()
driver.find_elements_by_tag_name()
driver.find_elements_by_link_text()
driver.find_elements_by_partial_link_text()
driver.find_elements_by_name()
driver.find_elements_by_id()