# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    list_comprehension.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/09 16:46:55 by anolivei          #+#    #+#              #
#    Updated: 2021/06/09 16:55:13 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# a list of integers
l_integers = [1,3,4,5,7,8,9]
print(l_integers)

# normal way to create a new list with pairs numbers
pairs = []
for number in l_integers:
	if number % 2 == 0:
		pairs.append(number)
print(pairs)

# list comprehension way to create a new list with pairs numbers
pairs = [number for number in l_integers if number % 2 == 0]
print(pairs)