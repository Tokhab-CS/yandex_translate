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
            print(parsing_data[i])
            parsing_dict(parsing_data[i])
    if isinstance(parsing_data, list):
        for i in parsing_data:
            print(i)
            parsing_dict(i)


if __name__ == '__main__':
    arr = [1, [[2]], [4]]
    print(parsing_list(arr))

    dict_train = {
        "result": {
            "tabs": [
                {
                    "pos": {
                        "code": "nn",
                        "text": "сущ",
                        "tooltip": "существительное"
                    },
                    "text": "repast",
                    "translation": {
                        "pos": {
                            "code": "nn",
                            "text": "сущ",
                            "tooltip": "существительное"
                        },
                        "text": "трапеза"
                    }
                },
                {
                    "pos": {
                        "code": "nn",
                        "text": "сущ",
                        "tooltip": "существительное"
                    },
                    "text": "repast",
                    "translation": {
                        "pos": {
                            "code": "nn",
                            "text": "сущ",
                            "tooltip": "существительное"
                        },
                        "text": "пиршество"
                    }
                }]}}

    parsing_dict(dict_train)
