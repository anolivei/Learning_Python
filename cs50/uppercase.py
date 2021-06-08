# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    uppercase.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 12:09:52 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 12:09:52 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cs50 import get_string

s = get_string("Before: ")
print ("After: {}".format(s.upper()))
