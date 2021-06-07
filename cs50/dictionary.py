# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dictionary.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/06 16:48:11 by anolivei          #+#    #+#              #
#    Updated: 2021/06/06 17:29:57 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

words = set()

def	check(word):
	if word.lower() in words:
		return True
	else:
		return False

def	load(dictionary):
	file = open(dictionary, "r")
	for line in file:
		words.add(line.rstrip("\n"))
	file.close()
	return True

def	size():
	return len(words)

def	unload():
	return True