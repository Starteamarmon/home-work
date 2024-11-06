# Задание 1
# Есть некоторый словарь, который хранит названия 
# странистолиц.Названиестраныиспользуетсявкачестве 
# ключа,названиестолицывкачествезначения.Необходимо 
# реализовать: добавлениеданных,удалениеданных,поиск 
# данных, редактирование данных, сохранение и загрузку 
# данных (используя упаковку и распаковку).
import json


class StethemJson:
    def __init__(self):
        self.dict = {}

    def load_json(self):
        # with open('json/stethem.json', 'r') as f:
        #     self.dict = json.load(f)
        try:
            with open('json/stethem.json', 'r') as f:
                self.dict = json.load(f)
        except FileNotFoundError:
            print(f"Файл 'json/stethem.json' не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка разбора JSON в файле 'json/stethem.json'.")

    def edd_json(self, country, capital):
        self.dict[country] = capital

    def save_json(self):
        with open('json/stethem.json', 'w') as f:
            json.dump(self.dict, f, indent=4)

a = StethemJson()
a.load_json()
a.edd_json('Deucheland', 'Berlin')
a.save_json() 

a.edd_json('Nihon','Tokyo')
a.save_json() 

a.edd_json('Montenegro','Podgorica')
a.save_json() 
