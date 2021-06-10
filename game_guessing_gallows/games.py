# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    games.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/08 18:58:26 by anolivei          #+#    #+#              #
#    Updated: 2021/06/10 00:58:37 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import guessing
import gallows

def choose_game():
	print("************************")
	print("*** Choose your game ***")
	print("************************\n")
	print("1 - Guessing\n2 - Gallows\n")
	game = int(input("Which game? "))
	print()
	if (game == 1):
		guessing.guessing()
	elif (game == 2):
		gallows.gallows()

if(__name__ == "__main__"):
	choose_game()