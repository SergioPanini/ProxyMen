from typing import Dict, TYPE_CHECKING, List
from fake_useragent import FakeUserAgent
import random

if TYPE_CHECKING:
    from objects import Proxy 

ua = FakeUserAgent()

def headers() -> Dict[str, str]:
    '''Возвращяет хедер'''

    headers = {
            'User-Agent': ua.random,
            'content-type': 'text/html;charset=utf-8',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
            }

    return headers

def get_randome_proxy(list_proxies: List['Proxy']) -> 'Proxy':
    if list_proxies:
        #print('generator proxy::', list_proxies)
        return random.choice(list_proxies).get_dict()
    return {}