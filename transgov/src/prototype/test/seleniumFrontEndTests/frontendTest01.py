from selenium import webdriver
import time

def failed():
	print "Testing Failed"
	browser.quit()
	quit()






# opens the browser to the local host
# requires the frontend running on the localhost
browser = webdriver.Chrome()
browser.get('http://localhost:8080')

# trys to find the search button and click it to get the result page
try:
	searchElement = browser.find_element_by_id("search")
	searchElement.click()
	print "Successfully clicked the search button"
except Exception as e:
	print "Failed to find the search button"
	failed()

# waits for the page to load
time.sleep(5)

# trys to find a search result
try:
	result = browser.find_element_by_class_name("title")
	print "Successfully found result"
except Exception as e:
	print "Failed to find Result"
	print e
	failed()
else:
	pass

# trys to find and click the home button
try:
	home = browser.find_element_by_id("logo")
	home.click()
	print "Successfully went Home"
except Exception as e:
	print "Failed to go Home"
	failed()

# trys to find and click the advanced search button
try:
	advancedSearch = browser.find_element_by_id("search1")
	advancedSearch.click()

	advancedSearchResult = browser.find_element_by_id("AdvancedSearch")

	print "Successfully found AdvancedSearch result"
except Exception as e:
	print "Failed to load AdvancedSearch"
	print e
	failed()


print "Front end testing Successfull"

browser.quit()


