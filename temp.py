import jmespath
import json
import requests

def search_in_dict(source_dict=None, desired_key=None):
    for i in source_dict.keys():
        # if i == 'text':
        print(i, '=', source_dict[i])
        if isinstance(source_dict[i], dict):
            search_in_dict(source_dict[i], desired_key)
        elif isinstance(source_dict[i], list):
            for ii in range(0, len(source_dict[i])):
                if isinstance(source_dict[i][ii], dict):
                    search_in_dict(source_dict[i][ii], desired_key)

if __name__ == '__main__':
    text = 'complete'
    respond = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=2048703991642255491&yum=1642255618671602095')
    search_in_dict(respond.json(), 2)
    # # Получаем определенный элемент
    # d = {"foo": {"bar-1": "baz"}}
    # print(jmespath.search('foo.bar', d))
    # # baz
    #
    # # С помощью подстановочного знака получаем все названия
    # d = {"foo": {"bar": [{"name": "one"}, {"name": "two"}]}}
    # print(jmespath.search('foo.bar[*].name', d))
    # # [“one”, “two”]
    # text = 'complete'
    # text1 = 'after consideration'
    # respond = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=2048703991642255491&yum=1642255618671602095')
    # print(respond.json())
    # respond1 = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=ru&srv=tr-text&text={text1}&type=syn%2Cant%2Cderiv%2Cregular&lang=en-ru&flags=1255&dict=en.syn%2Cen.ant%2Cen.deriv%2Cen-ru.regular&yu=2048703991642255491&yum=1642255618671602095')
    # # print(respond.json())
    # # json_dict = json.loads(respond.json())
    # # print(jmespath.search('en-ru', json_dict))
    # print(respond.json()['en-ru']['regular'][0]['tr'][0]['text'])
    # print(respond1.json()['en-ru']['regular'][0]['tr'][0]['text'])
    # print(type(respond1.json()))