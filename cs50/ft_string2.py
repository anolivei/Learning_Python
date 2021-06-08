# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_string2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 01:29:24 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 01:32:42 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cs50 import get_string

s = get_string("Input: ")
print("Output: ", end = "")
for c in s:
	print(c, end = "")
print()