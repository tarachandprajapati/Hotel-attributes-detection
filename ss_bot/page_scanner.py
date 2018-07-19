from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import numpy as np
url = "https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1FCAEoggJCAlhYSDNYBGhsiAEBmAEuuAEIyAEM2AEB6AEB-AELkgIBeagCAw&sid=bad4d980199d9b6b7015900dd30f297f&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1FCAEoggJCAlhYSDNYBGhsiAEBmAEuuAEIyAEM2AEB6AEB-AELkgIBeagCAw%3Bsid%3Dbad4d980199d9b6b7015900dd30f297f%3Bsb_price_type%3Dtotal%26%3B&ss=New+York%2C+New+York+State%2C+USA&em_ac_deal_option_clicked=1&checkin_year=2018&checkin_month=6&checkin_monthday=29&checkout_year=2018&checkout_month=6&checkout_monthday=30&no_rooms=1&group_adults=2&group_children=0&from_sf=1&ss_raw=New&ac_position=0&ac_langcode=en&dest_id=20088325&dest_type=city&place_id_lat=40.768074&place_id_lon=-73.981895&search_pageview_id=8e3046235fbd0018&search_selected=true&search_pageview_id=8e3046235fbd0018&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
driver = webdriver.Firefox(executable_path = "C:\geckodriver.exe")
def page_scanner(url, i):
	driver.get(url)
	dim = np.array([220, 890, 1460, 2130, 2780, 3400, 4600, 5100])
	for j in range(0,8): 
		driver.execute_script("window.scrollTo(0, "+str(dim[j])+");" )
		driver.save_screenshot(str(i)+_+str(j)+".png")
	driver.quit()