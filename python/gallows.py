# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gallows.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/08 19:16:48 by anolivei          #+#    #+#              #
#    Updated: 2021/06/09 13:03:27 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def gallows():
	print("***********************")
	print("*** Playing Gallows ***")
	print("***********************")
	
	secret_word = "vogons".lower()
	correct_letters = ["_", "_", "_", "_", "_", "_"]
	print(correct_letters)
	dead = False
	won = False
	while(not dead and not won):
		guessing = input("Choose a letter: ").lower().strip()
		i = 0
		for letter in secret_word:
			if(guessing == letter):
				print("Letter {} found in position {}".format(guessing, i))
				correct_letters[i] = guessing
				print(correct_letters)
			i += 1
		print("Playing...")

	print("Game Over")

if(__name__ == "__main__"):
	gallows()