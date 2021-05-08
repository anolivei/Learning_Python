# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    simple_game.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/06 21:38:47 by anolivei          #+#    #+#              #
#    Updated: 2021/05/08 17:55:53 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random as rd

secret_number = rd.randrange(0, 101)

guess = int(input("Type a number between 1 and 100: "))

game_try = 1

while (guess < 1 or guess > 100):
	print("Try number {}".format(game_try))
	print("You must choose a number between 1 and 100!")
	guess = int(input("Type a number between 1 and 100: "))
	game_try += 1

right = guess == secret_number

while (right == 0):
	if (guess < 1 or guess > 100):
		print("You must choose a number between 1 and 100!")
		continue
	higher	= guess > secret_number
	lower	= guess < secret_number
	if (higher):
		print("Try number {}".format(game_try))
		guess = input("It isn't the secret number, try a lower number: ")
	elif (lower):
		print("Try number {}".format(game_try))
		guess = input("It isn't the secret number, try a higher number: ")
	guess = int(guess)
	right = guess == secret_number
	game_try += 1
if (right):
	print("Yay, you're right, the secret number was {}, you spent {} tries to discovery it".format(secret_number, game_try))