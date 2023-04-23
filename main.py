from danger_car import DangerCar
from user_car import UserCar
from pit import Pit
from tkinter import *
import random

window = Tk()

user_car = UserCar(x=445, y=600, speed_1=0, file='images/car_1.png')

danger_car_1 = DangerCar(x=random.randint(320, 450), y=-100, speed_1=random.randint(1, 2), file='images/danger_1.png')
danger_car_2 = DangerCar(x=random.randint(320, 580), y=-700, speed_1=random.randint(1, 3), file='images/danger_2.png')
danger_car_3 = DangerCar(x=random.randint(320, 580), y=-1900, speed_1=random.randint(2, 3), file='images/danger_3.png')

pit_1 = Pit(x=random.randint(330, 410), y=random.randint(300, 550), file='images/pit.png')
pit_2 = Pit(x=random.randint(480, 570), y=random.randint(30, 400), file='images/pit.png')


def get_info():
    canvas.create_text(730, 530, text='Разработчик игры \"FunCars\" - Павел Фенёв', font='Arial 9', fill='green')


def select_color(color):
    global car_color
    car_color = color


def respawn(game_obj, game_obj_x, game_obj_y):
    game_obj.x = game_obj_x
    game_obj.y = game_obj_y


def get_finish_scene(text):
    canvas.delete('all')

    canvas.create_text(width / 2, height / 2, text=text, font='Arial 40', fill='red')

    respawn(user_car, 445, 600)

    respawn(game_obj=danger_car_1, game_obj_x=random.randint(320, 450), game_obj_y=-100)
    respawn(game_obj=danger_car_2, game_obj_x=random.randint(320, 580), game_obj_y=-700)
    respawn(game_obj=danger_car_3, game_obj_x=random.randint(320, 580), game_obj_y=-1900)

    respawn(game_obj=pit_1, game_obj_x=random.randint(330, 410), game_obj_y=random.randint(300, 550))
    respawn(game_obj=pit_2, game_obj_x=random.randint(480, 570), game_obj_y=random.randint(30, 400))

    back_button.place(width=220, height=75, x=340, y=410)


def create_menu():
    global car_color

    canvas.delete('all')
    back_button.place_forget()

    play_button.place(width=220, height=75, x=340, y=410)
    info_button.place(width=330, height=75, x=565, y=410)

    canvas.create_rectangle(350, 0, 550, 650, fill='grey')
    canvas.create_rectangle(435, 40, 455, 180, fill='white')
    canvas.create_rectangle(435, 220, 455, 360, fill='white')
    canvas.create_rectangle(435, 400, 455, 540, fill='white')
    canvas.create_rectangle(370, 70, 415, 170, fill='light blue')
    canvas.create_rectangle(480, 270, 525, 370, fill='red')

    canvas.create_polygon(650, 400, 850, 400, 750, 75, fill='brown')
    canvas.create_polygon(50, 400, 250, 400, 150, 75, fill='brown')

    canvas.create_oval(75, 75, 225, 225, fill='green')
    canvas.create_oval(670, 75, 830, 225, fill='green')

    canvas.create_text(780, 15, text='типо дерево', font='Arial 30', fill='green')
    canvas.create_text(115, 410, text='выбрать цвет машине:', font='Arial 16', fill='green')
    canvas.create_text(65, 15, text='победы: ' + str(wins_count), font='Arial 20', fill='green')

    canvas.create_line(760, 40, 760, 70, fill='red')
    canvas.create_line(760, 70, 775, 60, fill='red')
    canvas.create_line(760, 70, 745, 60, fill='red')

    color_button_1.place(width=50, height=50, x=5, y=425)
    color_button_2.place(width=50, height=50, x=60, y=425)
    color_button_3.place(width=50, height=50, x=115, y=425)

    car_color = 'grey'


def start_game():
    global back_button
    global wins_count

    canvas.delete('all')

    play_button.place_forget()
    info_button.place_forget()

    color_button_1.place_forget()
    color_button_2.place_forget()
    color_button_3.place_forget()

    canvas.create_rectangle(300, 0, 600, 650, fill='grey')
    canvas.create_rectangle(435, 40, 455, 180, fill='white')
    canvas.create_rectangle(435, 220, 455, 360, fill='white')
    canvas.create_rectangle(435, 400, 455, 540, fill='white')

    canvas.create_image(pit_1.x, pit_1.y, image=pit_1.image)
    canvas.create_image(pit_2.x, pit_2.y, image=pit_2.image)

    canvas.create_image(danger_car_1.x, danger_car_1.y, image=danger_car_1.image_1)
    canvas.create_image(danger_car_2.x, danger_car_2.y, image=danger_car_2.image_1)
    canvas.create_image(danger_car_3.x, danger_car_3.y, image=danger_car_3.image_1)

    color_dict = {
        'red': user_car.image_1,
        'green': user_car.image_2,
        'blue': user_car.image_3,
        'grey': user_car.image_4
    }

    canvas.create_image(user_car.x, user_car.y, image=color_dict[car_color])

    user_car.y += user_car.speed_1
    user_car.x += user_car.speed_2

    danger_car_1.y += danger_car_1.speed_1
    danger_car_2.y += danger_car_2.speed_1
    danger_car_3.y += danger_car_3.speed_1

    if user_car.y < 40:
        get_finish_scene('Ты победил(а)!')
        wins_count += 1
        return

    if user_car.is_crash(danger_car_1) or user_car.is_crash(danger_car_2) or user_car.is_crash(danger_car_3):
        get_finish_scene('Ты проиграл(а)')
        return

    if user_car.x < 315 or user_car.x > 585:
        get_finish_scene('Ты проиграл(а), съехав с дороги')
        return

    if user_car.is_crash(pit_1) or user_car.is_crash(pit_2):
        get_finish_scene('Ты проиграл(а), наехав на яму')
        return
    
    window.after(5, start_game)


width = 900
height = 650

window.title('FunCars')
window.geometry(str(width) + 'x' + str(height))

canvas = Canvas(window, width=width, height=height)
canvas.pack()

window.bind('<Key-Up>', user_car.move_up)
window.bind('<KeyRelease>', user_car.stop_move)
window.bind('<Key-Right>', user_car.move_right)
window.bind('<Key-Left>', user_car.move_left)

car_color = 'grey'

with open('wins_count.txt', 'r', encoding='UTF-8') as file:
    wins_count = int(file.read())

color_button_1 = Button(bg='red', command=lambda: select_color('red'))
color_button_2 = Button(bg='green', command=lambda: select_color('green'))
color_button_3 = Button(bg='blue', command=lambda: select_color('blue'))

info_button = Button(text='Информация', font=('Arial', 20), fg='white', bg='green', command=get_info)
play_button = Button(text='ИГРАТЬ', font=('Arial', 20), fg='white', bg='gold', command=start_game)
back_button = Button(text='В МЕНЮ', font=('Arial', 20), fg='white', bg='gold', command=create_menu)

create_menu()
window.mainloop()

with open('wins_count.txt', 'w', encoding='UTF-8') as file:
    file.write(str(wins_count))
