# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_int.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/06 18:43:48 by anolivei          #+#    #+#              #
#    Updated: 2021/06/06 18:47:28 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cs50 import get_int

age = get_int("What's your age?\n")
print(f"You are at least {age * 365} days old.")
print("You are at least {} days old.".format(age * 365))