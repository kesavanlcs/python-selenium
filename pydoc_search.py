import unittest, time
from selenium.webdriver.common.keys import Keys

from config import *

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = driver

    def test_search_in_python_org_pass(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)

    def test_search_in_python_fail(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python1212", driver.title)     
	  

    def tearDown(self):
        self.driver.close()
