# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    positive.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 15:04:21 by anolivei          #+#    #+#              #
#    Updated: 2021/06/07 16:04:30 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cs50 import get_int

def	main():
	i = get_positive_int()
	print(i)

def get_positive_int():
	while True:
		n = get_int("Positive Integer: ")
		if (n > 0):
			break
	return(n)

main()
