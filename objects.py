
from abc import ABC, abstractmethod
from typing import List

class Proxy:
    ip: str
    port: int
    type_: str
    secure: str

    class Meta:
        valid_types = ['http', 'https']

    def __init__(
            self,
            ip: str,
            port: int,
            type_: str = None,
            secure: str = None
        ):
        
        '''Создание прокси'''
        self.ip = ip
        self.port = port
        
        if port == 80:
            self.type_ = 'http'
        elif port == 443:
            self.type_ = 'https'
        else: 
            self.type_ = type_.lower()

        self.secure = secure

    def get_dict(self) -> dict:
        if self.type_ in self.Meta.valid_types:
            return {'http':f'{self.type_}://{self.ip}:{self.port}'}

        return {}

class AbstractLoader(ABC):
    '''Абстрактный класс поставщика прокси'''

    URL: str


    @abstractmethod
    def load(self, proxy_list: List[Proxy] = []) -> List[Proxy]:
        '''Метод возвращяет список с прокси'''
