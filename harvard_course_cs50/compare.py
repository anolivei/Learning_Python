# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    compare.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 16:36:23 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 16:38:14 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cs50 import get_string

s = get_string("s: ")
t = get_string("t: ")

if s == t:
	print("Same")
else:
	print("Different")