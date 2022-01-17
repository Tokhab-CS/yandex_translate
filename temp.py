import jmespath
import json
import requests

# Получаем определенный элемент
d = {"foo": {"bar-1": "baz"}}
print(jmespath.search('foo.bar', d))
# baz

# С помощью подстановочного знака получаем все названия
d = {"foo": {"bar": [{"name": "one"}, {"name": "two"}]}}
print(jmespath.search('foo.bar[*].name', d))
# [“one”, “two”]
text = 'inquiry'
text1 = 'after consideration'
respond = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=2048703991642255491&yum=1642255618671602095')
respond1 = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=ru&srv=tr-text&text={text1}&type=syn%2Cant%2Cderiv%2Cregular&lang=en-ru&flags=1255&dict=en.syn%2Cen.ant%2Cen.deriv%2Cen-ru.regular&yu=2048703991642255491&yum=1642255618671602095')
# print(respond.json())
# json_dict = json.loads(respond.json())
# print(jmespath.search('en-ru', json_dict))
print(respond.json()['en-ru']['regular'][0]['tr'][0]['text'])
print(respond1.json()['en-ru']['regular'][0]['tr'][0]['text'])