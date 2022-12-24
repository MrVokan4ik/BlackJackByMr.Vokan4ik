koloda = [ 6, 7, 8, 9, 10, 11]  * 4

import os
import random 
random.shuffle(koloda)

print('21 очко')
count = 0

print('Black Jack By Mr.Vokan4ik')
print('GitHub: https://github.com/MrVokan4ik/BlackJackByMrVokan4ik')
while True:
	choice = input('будете брать карту? y/n\n')
	if choice == 'y':
		current = koloda.pop()
		print('Вам попалась карта %d' %current)
		count += current
		
		if count >  21:
			print('Извените, но вы проиграли!')
			start = input('Будешь сново?y/n:\n')
			if start == 'y':
				os.startfile('blackjack.exe')
				break
			else:
				break
				
			
		elif count == 21:
				print('Поздравляю, вы набрали 21 очко!')
				start = input('Будешь сново?y/n:\n')
				if start =='y':
					os.startfile('blackjack.exe')
					break
				else:
					break
				
		else:
				print('У вас %d очков.' %count)
				
	elif choice == 'n':
		print('У вас %d очков и вы закончили игру.' %count)
		start = input('Будешь сново?y/n:\n')
		if start =='y':
			os.startfile('blackjack.exe')
			break
		else:
			break
		break
		