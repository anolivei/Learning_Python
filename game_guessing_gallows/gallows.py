# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gallows.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/08 19:16:48 by anolivei          #+#    #+#              #
#    Updated: 2021/06/10 00:55:09 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def gallows():
	print_welcome_mesage()
	create_file()
	secret_word = choose_secret_word()
	correct_letters = ["_" for letter in secret_word]
	dead = False
	won = False
	error = 0
	while (not dead and not won):
		guessing = import_guess()
		if (guessing in secret_word):
			put_correct_guess(secret_word, guessing, correct_letters)
		else:
			error += 1
			print_gallow(error)
		dead = error == 7
		won = "_" not in correct_letters
		print("You have {} more chances\n".format(7 - error))
		print(' '.join(correct_letters))
	if (won):
		print_winner_message()
	else:
		print_loser_message(secret_word)

def print_welcome_mesage():
	print("***********************")
	print("*** Playing Gallows ***")
	print("***********************\n")

def	create_file():
	with open("file.txt", "w") as file:
		file.write("Ring\n")
		file.write("Microwave\n")
		file.write("Welcome\n")
		file.write("Table\n")
		file.write("Tomorrow\n")
		file.write("Hobbit\n")

def choose_secret_word():
	with open("file.txt", "r") as file:
		words = []
		for line in file:
			line = line.strip()
			words.append(line)
	secret_word = words[random.randrange(0, len(words))].upper()
	return(secret_word)

def import_guess():
	guessing = input("Choose a letter: ").upper().strip()
	print()
	return (guessing)

def put_correct_guess(secret_word, guessing, correct_letters):
	i = 0
	for letter in secret_word:
		if (guessing == letter):
			correct_letters[i] = letter
		i += 1

def print_gallow(error):
	print("  _______     ")
	print(" |/      |    ")

	if(error == 1):
		print(" |      (_)   ")
		print(" |            ")
		print(" |            ")
		print(" |            ")

	if(error == 2):
		print(" |      (_)   ")
		print(" |      \     ")
		print(" |            ")
		print(" |            ")

	if(error == 3):
		print(" |      (_)   ")
		print(" |      \|    ")
		print(" |            ")
		print(" |            ")

	if(error == 4):
		print(" |      (_)   ")
		print(" |      \|/   ")
		print(" |            ")
		print(" |            ")

	if(error == 5):
		print(" |      (_)   ")
		print(" |      \|/   ")
		print(" |       |    ")
		print(" |            ")

	if(error == 6):
		print(" |      (_)   ")
		print(" |      \|/   ")
		print(" |       |    ")
		print(" |      /     ")

	if (error == 7):
		print(" |      (_)   ")
		print(" |      \|/   ")
		print(" |       |    ")
		print(" |      / \   ")

	print(" |            ")
	print("_|___         ")
	print()

def print_winner_message():
	print("\nCongratulations! You Won!")
	print("       ___________      ")
	print("      '._==_==_=_.'     ")
	print("      .-\\:      /-.    ")
	print("     | (|:.     |) |    ")
	print("      '-|:.     |-'     ")
	print("        \\::.    /      ")
	print("         '::. .'        ")
	print("           ) (          ")
	print("         _.' '._        ")
	print("        '-------'       ")

def print_loser_message(secret_word):
	print("\nGame Over")
	print("\nThe secret word was {}\n".format(secret_word))
	print("    _______________         ")
	print("   /               \       ")
	print("  /                 \      ")
	print("//                   \/\  ")
	print("\|   XXXX     XXXX   | /   ")
	print(" |   XXXX     XXXX   |/     ")
	print(" |   XXX       XXX   |      ")
	print(" |                   |      ")
	print(" \__      XXX      __/     ")
	print("   |\     XXX     /|       ")
	print("   | |           | |        ")
	print("   | I I I I I I I |        ")
	print("   |  I I I I I I  |        ")
	print("   \_             _/       ")
	print("     \_         _/         ")
	print("       \_______/           ")

if(__name__ == "__main__"):
	gallows()