# Задание 1
# Есть некоторый словарь, который хранит названия 
# странистолиц.Названиестраныиспользуетсявкачестве 
# ключа,названиестолицывкачествезначения.Необходимо 
# реализовать: добавлениеданных,удалениеданных,поиск 
# данных, редактирование данных, сохранение и загрузку 
# данных (используя упаковку и распаковку).
import json


# class StethemJson:
#     def __init__(self):
#         self.dict = {}

#     def load_json(self):
#         # with open('json/stethem.json', 'r') as f:
#         #     self.dict = json.load(f)
#         try:
#             with open('json/stethem.json', 'r') as f:
#                 self.dict = json.load(f)
#         except FileNotFoundError:
#             print("Файл 'json/stethem.json' не найден.")
#         except json.JSONDecodeError:
#             print("какая-то еррор 'json/stethem.json'.")

#     def edd_json(self, country, capital):
#         self.dict[country] = capital

#     def save_json(self):
#         with open('json/stethem.json', 'w') as f:
#             json.dump(self.dict, f, indent=4)

# a = StethemJson()
# a.load_json()
# a.edd_json('Deucheland', 'Berlin')
# a.save_json() 

# a.edd_json('Nihon','Tokyo')
# a.save_json() 

# a.edd_json('Montenegro','Podgorica')
# a.save_json()



# Задание 2
# Есть некоторый словарь, который хранит названия 
# музыкальных групп(исполнителей) и альбомов. Назва
# ние группы используется в качестве ключа, название 
# альбомов вкачестве значения.Необходимо реализовать: 
# добавление данных,+
# удаление данных,+
# поиск данных, +
# редактирование данных+
# сохранение и загрузку данных 
# (используя упаковку и распаковку).





class Collection:
    def __init__(self):
        self.my_dict: dict = {}

    def open_c(self):
        with open("home-work/json/Collection.json") as f:
            self.my_dict = json.load(f)

    def app_in_c(self,band : str ,album: str):
        self.my_dict[band] = album
        
    def search_c(self,band):
        menu = ''
        if band in self.my_dict:
            while menu != '3':
                print('1.Редактировать\n2.Удалить\n3.Выход')
                menu = input("Что мутим?: ")
                if menu == '1':
                    edit = input('Введите название альбома с изменениями: ')
                    self.my_dict[band] = edit
                    menu = '3'
                elif menu == '2':
                    del self.my_dict[band]
                    menu = '3'
                elif menu not in '123':
                    print('Такого пункта нет!')
        else:
            print('Нет такого исполнителя.')

    def save_с(self):
        with open('home-work/json/Collection.json', 'w') as f:
            json.dump(self.my_dict, f)

a = Collection()
a.app_in_c('Suicide Silence','The Black Crown')
a.app_in_c('Bring Me The Horizon','Suicide Season')
a.app_in_c('Slaughter to Prevail','Chapters of Misery')
a.search_c("Suicide Silence")
a.save_с()