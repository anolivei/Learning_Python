# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_string.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/06 17:36:18 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 00:40:28 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cs50 import get_string

s = get_string("What's your name?\n")
print("hello, " + s)
print(f"hello, {s}")
print("hello, {}".format(s))