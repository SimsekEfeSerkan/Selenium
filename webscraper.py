from selenium import webdriver

url = "https://www.zillow.com/homes/for_sale/Manhattan,-New-York,-NY_rb/"
browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath('xpath,//*[@id="zpid_2060136087"]/div/div[1]/a').click()

