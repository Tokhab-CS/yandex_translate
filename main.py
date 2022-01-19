from abc import ABC
from enum import Enum, auto

import jmespath
import json
import requests

class Translate(ABC):
    def action(self):
        pass

class TranslateEnRu(Translate):
    def action(self):
        print(f"We've translated some text from English to Russian")

class TranslateRuEn(Translate):
    def action(self):
        print("We've translated some text from Russian to English")

# class TranslateFactory(ABC):
#     def collect_data_from_site(self, text):
#         pass

class EnRuFactory:
    def collect_data_from_site(self, text):
        print(f'Translate "{text}" En -> Ru')
        return TranslateEnRu()

class RuEnFactory:
    def collect_data_from_site(self, text):
        print(f'Translate "{text}" Ru -> En')
        return TranslateRuEn()

#
# class ResultDictionary:
#     def __init__(self):
#         direction = None
#         source = None
#         translate = None
#         synonyms = None
#         declensions_and_conjugations = None
#         antonyms = None
#

def do_translate(entry):
    if entry == 'welcome':
        return EnRuFactory().collect_data_from_site(entry)
    elif entry == 'compete':
        return EnRuFactory().collect_data_from_site(entry)
    elif entry == 'привет':
        return RuEnFactory().collect_data_from_site(entry)
    else:
        return None

class TranslateDirection:
    class AvailableDirection(Enum):
        EnRu = auto()
        RuEn = auto()

    directions = []
    chosen = False

    def __init__(self):
        if not self.chosen:
            self.chosen = True
            for d in self.AvailableDirection:
                factory_name = d.name + 'Factory'
                factory_instance = eval(factory_name)()
                self.directions.append((d.name, factory_instance))

    def choose_direction(self):
        print('Available directions:')
        for f in self.directions:
            print(f[0])

        s = input(f'Please choose the direction (0-{len(self.directions)-1}): ')
        idx = int(s)
        s = input(f'What is text: ')
        text = s
        return self.directions[idx][1].collect_data_from_site(text)

if __name__ == '__main__':
    p = TranslateDirection()
    p.choose_direction().action()


    entry = input('What is the world would you like to translate? ')
    translate = do_translate(entry)
    translate.action()
