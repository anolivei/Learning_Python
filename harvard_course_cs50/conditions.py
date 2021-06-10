# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    conditions.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/06 18:48:08 by anolivei          #+#    #+#              #
#    Updated: 2021/06/06 21:19:22 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

if (x > y):
	print("x is greater than y")
elif (x < y):
	print("x is less than y")
else:
	print("x is equal to y")