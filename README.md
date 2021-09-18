# ProxyMen
Эта бибилиотека парсит прокси и предоставляет вам удобрый IPA для подачи прокси в `requests` что бы парсит другие сайты.

# Pull Requests
Вы можете писать свои лоадеры прокси и создавать пулл реквесты что бы внести свой вклад в open source и добавить парсеры новык прокси.

# Source
Парсинг прокси производится с этих сайтов:
- https://hidemy.name

# Usage

### Клонируйте репозиторий

`git clone https://github.com/SergioPanini/ProxyMen.git`

### Установите зависимости
`cd ProxyMan && pip install -r req.txt`

### Используйте прокси 
```
from ProxyMen.loaders import ProxyLoader

PL = ProxyLoader()
prxes = PL.load()

for i in prxes:
    if i.get_dict():
        print(i.get_dict())

print('Прокси готовы ', len(prxes))

````

Также можно, а даже желательно, передать свои прокси для парсинга прокси что бы сервер не заблочил Ваш IP адрес.

```
from ProxyMen.objects import Proxy
from ProxyMen.loaders import ProxyLoader

l = [Proxy(ip='<your ip>', port=<your port>, type_=<your type>), Proxy(ip='<your ip>', port=<your port>, type_=<your type>)]

PL = ProxyLoader(l)
prxes = PL.load()

for i in prxes:
    if i.get_dict():
        print(i.get_dict())

print('Прокси готовы ', len(prxes))

```
По умолчанию метод `get_dict()` отдает только `http` или `https` протоколы. А также что бы `requests` не ругался он заменяет префикс `https` на `http`. Если прокси не `http` или `https` то метод `get_dict` отдает `{}`.
