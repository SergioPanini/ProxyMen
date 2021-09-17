from .objects import Proxy, AbstractLoader
from typing import List, Optional
import requests
import bs4
from .utils import headers, get_randome_proxy
from time import sleep
import random

    
class ProxyLoader(AbstractLoader):
    '''Класс поставщика прокси'''

    URL: str = 'https://hidemy.name/ru/proxy-list/'

    def __init__(self, proxy_list: List[Proxy] = []):
        '''Инициализация'''
        self.proxy_list = proxy_list

    def load(self) -> List[Proxy]:
        '''Парсит прокси'''

        #Получаем пагинацию
        pagination = self._get_pagination
        print('[INFO] Pagination: ', pagination)

        #Ищем прокси
        result = []
        for page_number in range(0, pagination):
            
            #Загружаем страницу с прокси
            page = self._load_page(URL=self.URL  + '?start=%s' % (page_number * 64))
            
            if page:
                #Ищем прокси
                new_proxies = self._find_proxies_by_page(page)
            
                #Запоминаем прокси
                result.extend(new_proxies)

                #Расщиряем свой список с прокси что бы парси другие страници с прокси
                self.proxy_list.extend(result)

            else:
                print('Не удалось загрузить страницу ', self.URL  + '?start=%s' % (page_number * 64))
        return result
    
    def _load_page(self, URL: str) -> Optional[str]:
        '''Загружает страницу'''

        #Отправляем запрос 5 раз или пока ответ не равен ОК 
        status_code = 0
        times = 0
        while times < 5 and status_code != 200:
            p = get_randome_proxy(self.proxy_list)
            delay = random.randint(1, 2)/100
            print('Timeы: ', times, 'status_code: ', status_code, 'proxy:', p, 'URL', URL, 'delay', delay)
            sleep(delay)
            response = requests.get(URL, headers=headers(), proxies=p)
            
            #Увеличиваем счетчики
            times += 1
            status_code = response.status_code

        if status_code == 200:
            return response.text
        
        return None


    @property
    def _get_pagination(self) -> int:
        '''Ищет пагинацию'''

        page = self._load_page(self.URL)

        if page:
            
            #Находим пагинацию
            try:
                #Создаем страницу для парсера
                page = bs4.BeautifulSoup(page,'html.parser')
            
                return int(page.find(class_='pagination').find_all('a')[-2].text) 
            
            except AttributeError:
                pass
        
        return 0
        
    def _find_proxies_by_page(self, page: str) -> List[Proxy]:
        '''Находим прокси на странице'''
        
        #Создаем страницу для парсинга
        try:
            soup = bs4.BeautifulSoup(page,'html.parser')

            table_block = soup.find(class_='table_block')
            table_body = table_block.find('tbody')

            rows = table_body.find_all('tr')
        except:
            print('When find proxy it was error')
            return []

        #Парсим строки
        result = []
        for row in rows:
    
            try:
                data = row.find_all('td')
                ip = data[0].text
                port = data[1].text
                type_ = data[4].text
                secure = data[5].text
                result.append(Proxy(ip=ip, port=port, type_=type_, secure=secure))
        
            except AttributeError:
                print('When find proxy it was error')
        
        return result 