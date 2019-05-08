
from bs4 import BeautifulSoup as BSoup
from user_agent import generate_user_agent
import requests



def page_scraper(links):
	print('Cruises Pages scrap process...')
	result=[]
	for url in links:
		try:
			user_agent_ = {'User-Agent': generate_user_agent(device_type='desktop', os=('mac','linux'))}		
			print('scrap url page ...' + url[-30:-1]+'l')
			dict_result = {}
			ask = requests.get(url, headers = user_agent_)
			soup = BSoup(ask.content, 'html.parser')

			#Получение имени
			name = soup.find('div', class_='col-md-9 river-site-highlight').find('h1').get_text().split('\n')[0]
			dict_result.update({'name': name})

			#Получение количества дней
			soup_iter = soup.find('div', class_='panel-group accordion route').find_all('div', class_='panel panel-default')
			count_days = len(soup_iter)
			

			#Получение маршрутов
			itineary = [soup_item.find('span', class_="route-city").text.replace(' ', '').replace('\n', '') for soup_item in soup_iter]
			dict_result.update({'itineary': itineary})
			
			#Получение списка с датой отправки, кораблем, ценой
			soup_dayprice_iter = soup.find('div', class_='panel-group accordion price accordeon-data-price').find_all('div', class_='panel panel-default accordeon-panel-default')
			temp_list = []
			for soup_item in soup_dayprice_iter:
				tag_a = soup_item.find('a', class_='collapsed panel-title')							
				date_ = tag_a.find('div', class_= 'price-date').find('span', class_= 'price-duration').get_text()
				ship_ = tag_a.find('div', class_= 'price-ship').find('span').get_text()				
				price_ = tag_a.find('div', class_= 'price-ship').find('div', class_= 'pull-right').find('span', class_= 'big-table-font').text.replace(' ', '').replace('\n', '').replace('€', '').replace('.', '')			
				temp_list.append({date_converter(date_):{'ship':ship_, 'price':price_}})
			dict_result.update({'days': temp_list})		
			result.append(dict_result)
		except:
			print('Page ' + url[-30:-1]+'l'+ 'Not load')
	write_in_file(result)



def date_converter(date_str):
	return date_str.split(' - ')[0].replace('.', '').replace(' ', '-')


def write_in_file(result):
	import json
	print('Start write result')
	with open('result.txt', 'w+', encoding='utf8') as result_file:
		json.dump(result, result_file, indent=4, ensure_ascii=False)
	print('Результат записан в файл result.txt в каталоге со скриптом')




def main():
	print('Main Page scrap process...')
	links=[]
	user_agent_ = {'User-Agent': generate_user_agent(device_type='desktop', os=('mac','linux'))}
	_page_link='https://www.lueftner-cruises.com/en/river-cruises/cruise.html'
	ask = requests.get(_page_link, headers = user_agent_)
	soup = BSoup(ask.content, 'html.parser')
	links_soup = soup.find_all('span', class_='showYear2019 yearContainer')	
	for link in links_soup:	
		a = link.find('a')
		if a:
			links.append('https://www.lueftner-cruises.com' + a.get('href'))

	page_scraper(links[0:4])

if __name__ == '__main__':
	main()