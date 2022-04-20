# a = 1
# try:
#     a = 2
#     print(a)
#     raise Exception()
# except:
#     a = 3
#     print(a)
#     raise
# else:
#     a = 4
#     print(a)
# finally:
#     a = 5
#     print(a)

import requests


def parsing_list(arr):
    if len(arr) == 0:
        return arr
    if isinstance(arr[0], list):
        return parsing_list(arr[0]) + parsing_list(arr[1:])
    return arr[:1] + parsing_list(arr[1:])


def parsing_dict(parsing_data, upper_key=None):
    reult = []
    if isinstance(parsing_data, dict):
        for i in parsing_data:
            if i == 'rows':
                for ii in parsing_data[i]:
                    print(ii)
            # if i == 'tr':
            #     for ii in parsing_data[i]:
            #         print(ii['text'])

            # if i == 'syn':
            #     print(parsing_data[i][0]['text'])
            # if i == 'tr':
            #     print(parsing_data[i][0]['text'])

                # print(parsing_data[i])
            parsing_dict(parsing_data[i])
    if isinstance(parsing_data, list):
        for i in parsing_data:
            parsing_dict(i)


# text = 'send'
# dict_train = requests.get(
#     f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?sid=396bb4ba.61fa9989.a1435be1.74722d74657874&ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=5618489511536728465&yum=1536826203321897207')


def recur(n):
    if len(n) == 0:
        return n
    else:
        return n[0] + '-qq- ' + recur(''.join(n[1:]))


def find(element, json):
    keys = element.split('.')
    rv = json
    for key in keys:
        if isinstance(rv, list):
            rv = {str(i): rv[i] for i in range(0, len(rv))}
            # print('Watch here - ', rv)
            # print(type(rv), key)
        if rv != None: rv = rv.get(key)
    return rv


if __name__ == '__main__':
    j = {"app": {
        "Garden": {
            "Flowers": {
                "Red flower": "Rose",
                "White Flower": "Jasmine",
                "Yellow Flower": "Marigold"
            }
        },
        "Fruits": [{"Yellow fruit": "Mango"},
            {"Green fruit": "Guava"},
            {"White Flower": "groovy"}
        ],
        "Trees": {
            "label": {
                "Yellow fruit": "Pumpkin",
                "White Flower": "Bogan"
            }
        }
    }}
    list1 = [
        {'id': '1', 'name': 'test 1', 'slug': 'test1'},
        {'id': '2', 'name': 'test 2', 'slug': 'test2'},
        {'id': '3', 'name': 'test 3', 'slug': 'test3'},
        {'id': '4', 'name': 'test 4', 'slug': 'test4'},
        {'id': '5', 'name': 'test 5', 'slug': 'test4'}
    ]
    # print({str(i): list1[i] for i in range(0, len(list1))})
    # print(find('app.Fruits.1.Green fruit', j))

    # [
    # {
    #     "text": "educate",
    #     "pos": {
    #         "code": "vrb",
    #         "text": "гл",
    #         "tooltip": "глагол"
    #     },
    #     "ts": "ˈedjʊkeɪt",
    #     "prdg": {
    #         "irreg": False,
    #         "data": [
    #             {
    #                 "tables": 2
    #             }
    #         ]}}]

    # print({d["slug"]: d for d in list1})
    # print(dict((d["name"], d) for d in list1))
    # print({key: [i[key] for i in list1] for key in list1[0]})
    # print(find('app.Trees.label.White Flower', j))
    # arr = [1, [[2]], [4]]
    # print(parsing_list(arr))
    # text = 'educate'
    # li = ['as', 'aaa', 'ssa']
    # # print(recur(li))
    # # dict_train = requests.get(
    # # f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?sid=396bb4ba.61fa9989.a1435be1.74722d74657874&ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=5618489511536728465&yum=1536826203321897207')
    # print(find('en-ru.regular.text', dict_train.json()))
# print(find('app.Garden.Flowers.Red flower', j))
# parsing_dict(dict_train.json())
# print('')
# text = 'deploy'
    text = 'send'
    dict_train = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?sid=396bb4ba.61fa9989.a1435be1.74722d74657874&ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=5618489511536728465&yum=1536826203321897207')
    parsing_dict(dict_train.json())
    print(find('en-ru.regular.0.tr.0.text', dict_train.json()))
    print('Irreg - ', find('en-ru.regular.0.prdg.irreg', dict_train.json()))
    print(find('en-ru.regular.0.tr.1.text', dict_train.json()))
    print(find('en-ru.regular.0.tr.2.text', dict_train.json()))
    print(find('en-ru.regular.1.tr.1.text', dict_train.json()))
    print(find('en-ru.regular.2.tr.2.text', dict_train.json()))

    print(find('en.syn.0.tr.0.text', dict_train.json()))
    print(find('en.syn.0.tr.1.text', dict_train.json()))
    print(find('en.syn.0.tr.2.text', dict_train.json()))

# print('')
# text = 'sear'
# dict_train = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?sid=396bb4ba.61fa9989.a1435be1.74722d74657874&ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=5618489511536728465&yum=1536826203321897207')
# parsing_dict(dict_train.json())
# print('')
# text = 'beautiful'
# dict_train = requests.get(f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?sid=396bb4ba.61fa9989.a1435be1.74722d74657874&ui=ru&srv=tr-text&text={text}&type=regular%2Csyn%2Cant%2Cderiv&lang=en-ru&flags=7591&dict=en-ru.regular%2Cen.syn%2Cen.ant%2Cen.deriv&yu=5618489511536728465&yum=1536826203321897207')
# parsing_dict(dict_train.json())
