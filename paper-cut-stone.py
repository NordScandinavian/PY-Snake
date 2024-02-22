import random

winner = " "

choices = ['каменъ' , 'бумаrа' , 'ножницы']
pc_choice = random.choice(choices)

print('Привет! Это игра камень-ножницы-бумага!')

hum_choice = input('Камень, ножницы или бумага? ')

print('Компьтер выбирает', pc_choice)

if pc_choice == hum_choice:
   winner = "Ничья"
elif pc_choice == 'бумага' and hum_choice == 'камень':
    winner = 'Компьютер'
elif pc_choice == 'камень' and hum_choice == 'ножницы':
    winner = 'Компьютер'
elif pc_choice == 'ножницы' and hum_choice == 'бумага':
    winner = 'Компьютер'
else:
    winner = "Пользователь"

print(winner, ' win!')