import jmespath
import json
import requests

def translate(source_dict=None):
    result = []
    for i in range(0, len(source_dict['en-ru']['regular'])):
        for ii in range(0, len(source_dict['en-ru']['regular'][i]['tr'])):
            result.append(source_dict['en-ru']['regular'][i]['tr'][ii]['text'])
    return result

def add_data(source_dict=None, type_data=None):
    result = []
    for i in range(0, len(source_dict['en'][type_data])):
        for ii in range(0, len(source_dict['en'][type_data][i]['tr'])):
            result.append(source_dict['en'][type_data][i]['tr'][ii]['text'])
    return result

if __name__ == '__main__':
    text = 'inquiry'
    text = 'welcome'
    text = 'complete'
    respond = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=2048703991642255491&yum=1642255618671602095')
    print(translate(respond.json()))
    print('Synonyms - ', add_data(respond.json(), 'syn'))
    print('Deriv - ', add_data(respond.json(), 'deriv'))
    print('Antonims - ', add_data(respond.json(), 'ant'))

    text1 = 'after consideration'
    respond1 = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=ru&srv=tr-text&text={text1}&type=syn%2Cant%2Cderiv%2Cregular&lang=en-ru&flags=1255&dict=en.syn%2Cen.ant%2Cen.deriv%2Cen-ru.regular&yu=2048703991642255491&yum=1642255618671602095')
    print(translate(respond1.json()))
    print(add_data(respond1.json(), 'syn'))
    print(add_data(respond1.json(), 'deriv'))
    print(add_data(respond1.json(), 'ant'))




    # for i in range(0, len(respond.json()['en-ru']['regular'])):
    #     translate(respond.json()['en-ru']['regular'][i]['tr'])
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