from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.iu91.com/rs/rent/")
#assert "Python" in driver.title
elem = driver.find_element_by_class_name("showSwitcher")
#elem.clear()
elem.send_keys("QC")
elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()
