# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guessing.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/06 21:38:47 by anolivei          #+#    #+#              #
#    Updated: 2021/06/10 01:10:02 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random as rd

def guessing():

	print_welcome_message()
	secret_number = rd.randrange(1,101)
	guess = int(input("Type a number between 1 and 100: "))
	print()
	points = 1000
	game_try = 1
	while (guess < 1 or guess > 100):
		print("Try number {}\n".format(game_try))
		points -= abs(secret_number - guess)
		guess = retry_input()
		game_try += 1
	right = guess == secret_number
	while (right == 0):
		if (guess < 1 or guess > 100):
			guess = retry_input()
			points -= abs(secret_number - guess)
			continue
		higher	= guess > secret_number
		lower	= guess < secret_number
		if (higher):
			print("Try number {}\n".format(game_try))
			points -= abs(secret_number - guess)
			guess = input("It isn't the secret number, try a lower: ")
			print()
		elif (lower):
			print("Try number {}\n".format(game_try))
			points -= abs(secret_number - guess)
			guess = input("It isn't the secret number, try a higher one: ")
			print()
		guess = int(guess)
		right = guess == secret_number
		game_try += 1
	if (right):
		print("Yay, you're right, the secret number was {}, you spent {} tries to discovery it, your score is {}".format(secret_number, game_try, points))

def print_welcome_message():
	print("************************")
	print("*** Playing Guessing ***")
	print("************************\n")

def	retry_input():
	print("You must choose a number between 1 and 100!\n")
	guess = int(input("Type a number between 1 and 100: "))
	print()
	return(guess)

if(__name__ == "__main__"):
	guessing()