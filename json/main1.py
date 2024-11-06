from __future__ import annotations
import pickle
import json
# Задание 1
# К уже реализованному классу «Автомобиль» добавьте 
# возможность паковки и распаковки данных с использованием json и pickle

# class Auto:
#     def __init__(self,brand:str ,name:str ,year:int ,volume:float ,color:str ,price:int ):
#         self._name: str = name
#         self._year: int = year
#         self._brand: str = brand
#         self._volume: float = volume
#         self._color: str = color
#         self._price: int = price
#         self.dict: dict = {}

#     def __str__(self):
#         return f'Название тачки {self._brand} {self._name}, она {self._year} года выпуска, объём её дрыгателя составлет\n{self._volume} литра, она окрашена в сексуальный {self._color} цвет, и все это превосходство стоит {self._price} рублей'
    
#     def editAuto(self):
#         print('1 Бренд\n2 Модель\n3 Обьём\n4 Год\n5 Цвет\n6 Цена')
#         menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#         while menu != 7:
#             if menu == "1":
#                 self._brand = input('Введите название бренда с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '2':
#                 self._name = input('Введите название модели с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '3':
#                 self._volume:float = input('Введите объём двигателя с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '4':
#                 self._year = input('Введите год выпуска с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '5':
#                 self._color = input('Введите цвет авто с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu =='6':
#                 self._price = input('Введите стоимость авто с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 7 чтобы выйти: ')
#             elif menu == '7':
#                 return (self)
#     def info(self):
#         print('1 Бренд\n2 Модель\n3 Обьём\n4 Год\n5 Цвет\n6 Цена')
#         menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#         while menu != 7:
#             if menu == "1":
#                 print(self._brand)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '2':
#                 print(self._name)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '3':
#                 print(self._volume)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '4':
#                 print(self._year)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '5':
#                 print(self._color)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu =='6':
#                 print(self._price)
#                 menu = input('введите номер поля которое хотите увидеть, или 7 чтобы выйти: ')
#             elif menu == '7':
#                 return (self)
            
#     def inro(self):
#         self.dict[f'{self._brand} {self._name}'] = f'{self._year} года выпуска, объём её дрыгателя составлет\n{self._volume} литра, она окрашена в сексуальный {self._color} цвет, и все это превосходство стоит {self._price} рублей'
#         with open('home-work/json/auto.json','w') as f:
#             json.dump(self.dict,f)
#         return 'Еее'


#     def get_json(self):
#         with open("home-work/json/auto.json") as f:
#             self.my_dict = json.load(f)
#             print(self.dict)

# integra = Auto('Honda','Integra',2001,2.0,'Белый',900000)
# print(integra)
# integra.inro()
# integra.get_json()

# Задание 2
# К уже реализованному классу «Книга» добавьте возможность
# упаковки и распаковки данных с использова
# нием json и pickle.


# class Book:
#     def __init__(self,name:str ,year:int ,publisher:str ,genre:str ,author:str ,price:int ):
#         self._name:str = name
#         self._year:int = year
#         self._publisher:str = publisher
#         self._genre:str = genre
#         self._author:str = author
#         self._price:int = price

#     def pickle(self):
#         return pickle.dumps(self)
    
#     def __str__(self):
#         return f'{self._name}\n{self._year} года выпуска\nАвтор: {self._author}\nЖанр: {self._genre}\nИздатель: {self._publisher}\nЦена: {self._price} р.'
    
#     def in_file(self):
#         with open('home-work/json/dick.pickle', 'wb') as f:
#         	pickle.dump(self, f)

#     @staticmethod
#     def from_pickle():
#     	with open('home-work/json/dick.pickle', 'rb') as f:
#     		return pickle.load(f)        
    
#     def editBook(self):
#         print('1 Название\n2 Год выпуска\n3 Жанр\n4 Издатель\n5 Цена')
#         menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#         while menu != "6":
#             if menu == "1":
#                 self._name = input('Введите название книги с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '2':
#                 self._year = input('Введите год с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '3':
#                 self._genre:float = input('Введите жанр с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '4':
#                 self._publisher = input('Введите издателя с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '5':
#                 self._price = input('Введите стоимость с изменениями: ')
#                 menu = input('введите номер поля которое хотите изменить, или 6 чтобы выйти: ')
#             elif menu == '6':
#                 return (self)
            

#     def info(self):
#         print('1 Название\n2 Год выпуска\n3 Жанр\n4 Издатель\n5 Цена')
#         menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#         while menu != "6":
#             if menu == "1":
#                 print(self._name)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '2':
#                 print(self._year)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '3':
#                 print(self._genre)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '4':
#                 print(self._publisher)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '5':
#                 print(self._price)
#                 menu = input('введите номер поля которое хотите увидеть, или 6 чтобы выйти: ')
#             elif menu == '6':
#                 return (self)

# animal_farm = Book('Скотный двор',1945,'Harvill Secker',"Сатира","Джордж Оруэлл",102)
# print(animal_farm)

# animal_farm.in_file()
# a = Book.from_pickle()
# print(a)


# Задание 3
# К уже реализованному классу «Стадион» добавьте 
# возможность упаковки и распаковки данных с исполь
# зованием json и pickle.


class Stadium:
    def __init__(self,name:str ,date:str ,country:str ,city:str ,capacity:int ):
        self._name:str = name
        self._date:str = date
        self._country:str = country
        self._city:str = city
        self._capacity:int = capacity



    def __str__(self):
        return f'Станион {self._name}\nДата открытия: {self._date}\nСтрана: {self._country}\nГород: {self._city}\nВместимость: {self._capacity}'


    def info(self):
        print('1 Имя\n2 дата\n3 Страна\n4 Город\n5 Вместимость\n6 Выход')
        menu = input('Какое поле вывести?: ')
        while menu != '6':
            if menu == '1':
                print(self._name)
                menu = input('Какое поле вывести?: ')
            elif menu == '2':
                print(self._date)
                menu = input('Какое поле вывести?: ')
            elif menu == '3':
                print(self._country)
                menu = input('Какое поле вывести?: ')
            elif menu == '4':
                print(self._city)
                menu = input('Какое поле вывести?: ')
            elif menu == '5':
                print(self._capacity)
                menu = input('Какое поле вывести?: ')
            elif menu == '6':
                return(self)
            
    def in_txt(self):
        with open('home-work/json/stadion.txt','w',encoding='utf-8') as f:
            f.writelines(f'{self._name},{self._date},{self._country},{self._city},{self._capacity}')

    @staticmethod
    def from_txt():
        with open('home-work/json/stadion.txt','r',encoding='utf-8') as f:
            f.read(

            )
stadium = Stadium('Центральный','29.10.1967г','Россия','Красноярск',15000)#я тут подумал, вот метод ввода данных
print(stadium)#вот метод вывода данных

stadium.in_txt()
a = Stadium.from_txt()