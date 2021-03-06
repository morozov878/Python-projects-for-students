"""
Вступление
В этом проекте вы будете использовать веб-сервис,
чтобы узнать текущее местоположение Международной космической станции (МКС)
и нанести на карту его местоположение на карте.

Кто сейчас в космосе?
Вы собираетесь использовать веб-сервис,
который предоставляет оперативную информацию о космосе.
Во-первых, давайте выясним, кто сейчас находится в космосе.

Веб-сервис имеет адрес (URL), как и веб-сайт.
Но вместо того, чтобы возвращать HTML для веб-страницы,
он возвращает данные.

Откройте веб-сервис
http://api.open-notify.org/astros.json
в веб-браузере.

Данные в реальном времени.
Формат данных называется JSON (произносится как «Джейсон»).

Что такое JSON?
JSON - это формат для хранения и обмена данными.
JSON расшифровывается как JavaScript Object Notation,
что значит форма записи объектов в языке JavaScript,
но эта форма используется не только с JavaScript.

JSON - это текстовый формат, который можно использовать в коде, и его довольно легко читать.

"""

import json  # Импортируем модуль, позволяющий работать с файлами в формате json
import turtle  # Импортируем модуль черепаха для работы с картой
import urllib.request  # Импортируем модуль, позволяющий работать с URL адресами и позволяющий считывать информацию, хранящуюся по этому адресу
from PIL import Image
import time

url ='http://api.open-notify.org/astros.json'  # Запишем URL требуемый адрес
response = urllib.request.urlopen(url)  # Обращаемся по указанному веб адресу
result = json.loads(response.read())  # Прочитаем содержимое файла по указанному адресу
print(result)  # Выведем на экран это содержимое
"""
Содержимое файла astros.json предстваляет собой словарь,
в котором указывается текущее количество комсонавтов и астронавтов на орбите, их имена и корабль,
на котором они находятся в данный момент
Значение по ключу message показывает результат запроса к веб-странице
"""
print("Количество людей в космосе сейчас: ", result['number'])  # Выведем количество людей сейчас на орбите

people = result['people']
print(people)  # Выведем список людей на орбите, состоящий из трех словарей

for p in people:
    print(p['name'])  # Выведем имена космонавтов

"""
Сейчас хорошо попросить учеников аналогично вывести на экран название космического корабля,
на котором находится каждый космонавт
"""
for p in people:
    print(p['craft'])  # Вот так
"""
Где находится МКС?
Международная космическая станция находится на орбите вокруг Земли. 
Она проходит орбиту Земли примерно каждые полтора часа и движется 
со средней скоростью 7,66 км в секунду. Это быстро!
Давайте использовать другой веб-сервис, чтобы узнать, 
где находится Международная космическая станция.

Сначала откройте URL-адрес веб-службы на новой вкладке в веб-браузере:
http://api.open-notify.org/iss-now.json
Результат содержит координаты точки на Земле, 
над которым МКС в настоящее время находится.
Содержимое будет что0то вроде:
{
"iss_position": {
  "latitude": 8.54938193505081,
  "longitude": 73.16560793639105
},
"message": "success",
"timestamp": 1461931913
}
Широта и долгота
Широта и долгота используются,
чтобы дать координаты местоположениям на поверхности Земли.
Широта указывает положение вдоль осей север-юг и может быть любым значением от 90 до -90.
0 отмечает экватор.
Долгота указывает положение вдоль оси восток-запад и может принимать любое значение от -180 до 180. 
0 обозначает главный меридиан, который проходит через Гринвич в Лондоне, Великобритания.
Координаты даны как (широта, долгота). 
Координаты Королевской обсерватории в Гринвиче: (51.48, 0). Как видите, широта (север-юг) указывается первой.
Широту и долготу вашего положения можно узнать в онлайн-картах Google или Yandex, например, через тот же самый URL.
Теперь вам нужно вызвать тот же веб-сервис из Python.
"""
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
location = result['iss_position']
latitude = float(location['latitude'])  # Сохраним и выведем на экран текущую широту МКС
longitude = float(location['longitude'])  # Сохраним и выведем на экран текущую долготу МКС
print('Широта: ', latitude)
print('Долгота: ', longitude)
"""
Было бы полезно показать положение МКС на карте. 
Вы можете сделать это с помощью графики Python Turtle!
Теперь необходимо добавить в проект изображение карты мира
Необходимо скачать файл из интернета.
Например: https://commons.wikimedia.org/wiki/File:Mercator-projection.jpg
После скачивания его необходимо добавить в папку текущего проекта Pycharm
"""
screen = turtle.Screen()
screen.setup(774, 600)
screen.setworldcoordinates(-180, -90, 180, 90)
im = Image.open('map.gif')  # На всякий случай делать вот так через модуль PIL (Pillow).
                            # Если он вдруг не установлен у учеников,
                            # то его надо будет установить
im.save('map2.gif')  # Такой подход работает. Если напрямую вписать имя файла в bgpic, то может
                    # появиться ошибка чтения
screen.bgpic('map2.gif')  # Функция bgpic поодерживает только gif файлы
"""
Теперь надо скачать спрайты для нашей программы
Это можно сделать, например, здесь:
https://www.flaticon.com/
Нам понадобится спрайт МКС (спутника - satelite)
"""
screen.register_shape('space.gif')
iss = turtle.Turtle()
iss.shape('space.gif')

iss.penup()
iss.speed(1)
iss.goto(longitude, latitude)  # Переместим МКС в ее текущие координаты. Сначала долготу, потом широту
"""
Когда МКС будет над головой?
Существует также веб-сервис, 
который вы можете использовать, чтобы узнать, 
когда МКС будет в следующем конкретном месте.
"""
Moscow_latitude = 45.657544  # Московская широта (C поправкой)
Moscow_longitude = 37.757259  # Московская долгота
screen.register_shape('marker.gif')
location = turtle.Turtle()
location.speed(1)
location.shape('marker.gif')
location.penup()
location.goto(Moscow_longitude, Moscow_latitude)  # Перемещаем маркер в московские координаты
"""
Теперь давайте узнаем дату и время, когда МКС будет следующей накладной.
Как и раньше, вы можете вызвать веб-сервис, введя его URL в адресную строку веб-браузера:
api.open-notify.org/iss-pass.json

Этот веб-сервис принимает значения широты и долготы, 
поэтому вы должны включить их в URL. 
Входные данные добавляются после '?' и отделяется с помощью '&'.

Ответ включает в себя несколько переходов, и мы просто рассмотрим первый. 
Время указывается как метка времени Unix 
(вы сможете преобразовать его в удобочитаемое время в вашем скрипте Python).

Метки времени Unix - это удобный способ сохранить дату и время в виде одного числа.
Метка времени Unix - это количество секунд с 1 января 1970 года в UTC (международный стандарт времени). 
Например, 1498734934 - 29 июня 2017 года в 11:15.
Вы можете найти текущую метку времени Unix на 
unixtimestamp.com
"""
url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(Moscow_latitude) + '&lon=' + str(Moscow_longitude)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
"""
Нам понадобится модуль time Python, 
чтобы мы могли распечатать его в удобочитаемой форме и преобразовать в местное время. 
Тогда мы получим код, чтобы написать время передачи для Москвы.
"""
# Выводим результат на экран
over = result['response'][1]['risetime']
location.color("white")
location.write(time.ctime(over))

turtle.done()  # Не даем окну закрыться
