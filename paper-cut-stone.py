import random
hum_choice = ' '
winner = " "

choices = ['каменъ' , 'бумага' , 'ножницы']
pc_choice = random.choice(choices)

print('Привет! Это игра камень-ножницы-бумага!')
while (hum_choice != 'бумага' and 
    hum_choice != 'камень' and 
    hum_choice != 'ножницы'):
    hum_choice = input('Камень, ножницы или бумага? ')

if pc_choice == hum_choice:
   winner = 'Ничья'
elif pc_choice == 'бумага' and hum_choice == 'камень':
    winner = 'Компьютер'
elif pc_choice == 'камень' and hum_choice == 'ножницы':
    winner = 'Компьютер'
elif pc_choice == 'ножницы' and hum_choice == 'бумага':
    winner = 'Компьютер'
else:
    winner = "Пользователь"

if winner == 'Ничья':
    print( 'Мы оба выбрали ' , pc_choice + ' , играем снова .' )
else :
    print( winner , ' выиграл , я выбрал ' , pc_choice + '. ')