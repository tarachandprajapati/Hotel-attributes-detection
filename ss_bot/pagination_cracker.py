#Importing required dependencies
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
#URL once needed to pass inorder to get the coordinates of Next page button location 
url = "https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1FCAEoggJCAlhYSDNYBGhsiAEBmAEuuAEIyAEM2AEB6AEB-AELkgIBeagCAw&sid=bad4d980199d9b6b7015900dd30f297f&sb=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Flabel%3Dgen173nr-1FCAEoggJCAlhYSDNYBGhsiAEBmAEuuAEIyAEM2AEB6AEB-AELkgIBeagCAw%3Bsid%3Dbad4d980199d9b6b7015900dd30f297f%3Bsb_price_type%3Dtotal%26%3B&ss=New+York%2C+New+York+State%2C+USA&em_ac_deal_option_clicked=1&checkin_year=2018&checkin_month=6&checkin_monthday=29&checkout_year=2018&checkout_month=6&checkout_monthday=30&no_rooms=1&group_adults=2&group_children=0&from_sf=1&ss_raw=New&ac_position=0&ac_langcode=en&dest_id=20088325&dest_type=city&place_id_lat=40.768074&place_id_lon=-73.981895&search_pageview_id=8e3046235fbd0018&search_selected=true&search_pageview_id=8e3046235fbd0018&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0"
def get_next_url(url, page_num):
	request = Request(url)
	response = urlopen(request)
	#getting html document of the page inorder to get the url behind the button
	html_doc = response.read() 
	#soupify the document inorder to get the required tag where our required url is present
	soup = BeautifulSoup(html_doc, "html5lib")
	div_paging = soup.find('div', class_ = 'results-paging')
	a = div_paging.find('a', class_ = 'paging-next ga_sr_gotopage_'+str(page_num)+'_67')
	#Scraping the url from the found required tag
	url = a['href']
	#loc = a.location
	#print(div_paging)
	#print(url)
	response.close()
	return url
#u=get_next_url(url)
#print(u)
#u="https://www.booking.com/searchresults.en-gb.html?dest_id=20088325&dest_type=city&ss=New%2BYork%2C%2BNew%2BYork%2BState%2C%2BUSA&offset=15"
#get_next_url(u)
for page_num in range (2, 40):
	#url = url
	url = get_next_url(url, page_num)
	page_num = page_num + 1
	print(url)

