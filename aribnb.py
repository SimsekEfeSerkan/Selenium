from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#belirtilen sayfaya gider
driver = webdriver.Chrome()

driver.get("https://www.zillow.com/manhattan-new-york-ny/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A40.877483%2C%22south%22%3A40.683935%2C%22east%22%3A-73.910408%2C%22west%22%3A-74.047237%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12530%2C%22regionType%22%3A17%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D")

ronaldo = driver.find_element(By.NAME, "q")
#arama kutusuna ronaldo yazdırır,anahtarlar, selenium.webdriver.common.keys'ten içe aktarılan Keys sınıfı kullanılarak gönderilebilir
ronaldo.send_keys("ronaldo")
ronaldo.send_keys(Keys.RETURN)
#driver.find_element(By.NAME, "q").send_keys("ronaldo")

assert "No results found." not in driver.page_source
driver.close()