#start
#game "millionaire"
import keyboard

game_on = True

def greeting():
    print('Привет, будущий миллионер!')
    with open('rules.txt', encoding='utf-8') as f:
        greet = f.read()
        print(greet)

def on_key_press(event):
    if event.name == 'esc':
        game_on= False

keyboard.on_press(on_key_press)

while game_on:
    greeting()
    keyboard.wait()