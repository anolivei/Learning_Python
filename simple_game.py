# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    simple_game.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/06 21:38:47 by anolivei          #+#    #+#              #
#    Updated: 2021/05/06 22:05:25 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

secret_number = 42

guess = input("Type your number: ")
guess = int(guess)

while (secret_number != guess):
	guess = input("It isn't the secret number, try again: ")
	guess = int(guess)
if (secret_number == guess):
	print("Yay, you're right, the secret number was" , secret_number)