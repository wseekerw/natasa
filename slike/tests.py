from django.test import TestCase
from selenium import webdriver


# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.maximize_window()
# navigate to the application home page
driver.get("https://magento.com/search/gss")
# get the search textbox
search_field = driver.find_element_by_name("keys")
search_field.clear()
# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()
# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_xpath("//div[@class='result-title']/a")
# get the number of anchor elements found
print "Found " + str(len(products)) + " products:"
# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print product.text
# close the browser window
driver.quit()