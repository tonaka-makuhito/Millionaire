#start
#game "millionaire"

def greeting():
    print('Привет, будущий миллионер!')
    with open('rules.txt', encoding='utf-8') as f:
        greet = f.read()
        print(greet)
        
greeting()