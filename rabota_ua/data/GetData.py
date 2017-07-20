import requests, csv
from bs4 import BeautifulSoup

def get_html(url):
	r = requests.get(url)
	return r.text

def get_total_pages(html):
	soup = BeautifulSoup(html, 'lxml')
	try:
		page_count = soup.find('dl', class_ = 'f-pagination').find_all('dd')[-2].find('a').text.strip()
		return page_count
	except:
		return 1

def get_data(html):
	soup = BeautifulSoup(html, 'lxml')
	offers = soup.find_all('article', class_ = 'f-vacancylist-vacancyblock')
	for offer in offers:

		title = offer.find('a', class_ = 'ga_listing').text.strip()
		company = offer.find('p', class_ ='f-vacancylist-companyname').text.strip()
		try:
			price = offer.find('p', class_ = '-price').text.strip()
		except:
			price = ''
		data = {'title': title, 'company_name': company, 'price': price}
		write_csv(data)
def write_csv(data):
	with open('rabota_ua.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data['title'], data['company_name'], data['price']))	




def write(url):
	
	html = get_html(url)
	pages = get_total_pages(html)
	data = get_data(html)
	if int(pages) > 1:
		for i in range(1, int(pages) + 1):
			url+= '&pg=' + str(i)
			html = get_html(url)
			data = get_data(html)
			print('Обрабатывается страница ' + str(i))
	print('Обработано ' + str(pages) + ' страниц поиска')


