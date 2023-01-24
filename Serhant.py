import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.zillow.com/homes/for_sale/Manhattan,-New-York,-NY_rb/")
        self.assertIn("Zillow", driver.title)
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()