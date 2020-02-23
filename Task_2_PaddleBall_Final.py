from tkinter import *  # Импортируем содержимое модуля tkinter, который позволит нам работать с оконным приложением нашей будущей игры
import random  # Импортируем модуль random, он понадобится в нашей игре чуть позже
import time  # Импортируем модуль time, он понадобится нам чуть позже в нашей игре


class Ball:
    def __init__(self, canvas, paddle, color):  # Напишем функцию, которая будет создавть новый объект класса Ball
        self.canvas = canvas  # Закрепим наш мяч за используемым холстом
        self.paddle = paddle  # Закрепим наш мяч за используемой ракеткой
        self.form = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.form, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False  # Создадим флаг касания дна холста, который будет показывать момент когда мы проиграем

    def hit_paddle(self, pos):  # Напишем функцию удара ракеткой по мячу
        paddle_pos = self.canvas.coords(self.paddle.form)  # Аналогично с мячом сохраним текущее положение ракетки
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:  # Условие по X попадания ракетки по мячу
            if paddle_pos[1] <= pos[3] <= paddle_pos[3]:  # Условие по Y попадания ракетки по мячу
                return True  # В случае попадания ракетки по мячу возвращаем True
        return False  # В протиповоложном случае возвращаем False

    def draw(self):
        self.canvas.move(self.form, self.x, self.y)
        pos = self.canvas.coords(self.form)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:  # Изменение направления мяча в случае попадания ракетки по мячу
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


# Напишем класс ракетка
class Paddle:
    def __init__(self, canvas, color):  # Напишем функцию, которая будет создавать объект класса ракетка
        self.canvas = canvas  # Закрепим ракетку за нашим холстом
        self.form = canvas.create_rectangle(0, 0, 100, 10, fill=color)  # Настроим форму ракетки
        self.canvas.move(self.form, 200, 300)  # Настроим начальное положение ректки на холсте
        self.x = 0  # Зададим начальную скорость ракетки по горизонтали (вначале ракетка находится на месте)
        self.canvas_width = self.canvas.winfo_width()  # Передадим ракетке информацию о ширине холста
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)  # Привяжем событие нажатия на клавишу "стрелка влево" с движением ракетки влево
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)  # Привяжем событие нажатие на клавишу "стрелка вправо" с движением ракетки вправо

    def draw(self):  # Напишем функцию изображения ракетки на холсте
        self.canvas.move(self.form, self.x, 0)  # Определение перемещения ракетки по холсту. Ракетка должна перемещаться только по горизонтали
        pos = self.canvas.coords(self.form)  #
        if pos[0] <= 0:  # В случае касания ракетки левого края холста ракетка останавливается
            self.x = 0
        elif pos[2] >= self.canvas_width:  # В случае касания ракетки правого края холста ракетка останавливается
            self.x = 0

    def turn_left(self, evt):  # В случае появления события нажатия клавиши стрелка влево вызывается данная функция
        self.x = -2

    def turn_right(self, evt):  # В случае появления события нажатия клавиши стрелка вправо вызывается данная функция
        self.x = 2


game = Tk()
game.title("Скачущий мяч")
game.resizable(0, 0)
game.wm_attributes("-topmost", 1)
canvas = Canvas(game, width=500, height=400, bd=0,
                highlightthickness=0)
canvas.pack()
game.update()

paddle = Paddle(canvas, 'blue')  # Создадим объект ракетка
ball = Ball(canvas, paddle, 'red')  # Создадим объект мяч

while 1:
    if ball.hit_bottom == False:  # Если мы еще не проиграли
        ball.draw()
        paddle.draw()
    game.update_idletasks()
    game.update()
    time.sleep(0.01)
