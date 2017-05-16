import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ComparaMejorQuoteTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://comparamejor.com/")

    def test_quotation_in_funnel(self):
        driver = self.driver
        self.assertIn("Cotizar seguro para vehículo y compra SOAT | ComparaMejor.com", driver.title)
        quote_button = driver.find_element_by_id("quote-button")
        self.assertTrue(quote_button.is_displayed(), "Quote button is not visible")
        car_id = driver.find_element_by_id("quote")
        car_id.send_keys("ABC123")
        car_id.send_keys(Keys.RETURN)
        WebDriverWait(driver, 20)
        cmuj_selector = driver.find_element_by_id("uj40")
        self.assertTrue(cmuj_selector.is_displayed(), "Car type selector is not visible")
        car_icon = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath("//i[@class='cmuj-car']"))
        car_icon.click()
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
