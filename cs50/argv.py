# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    argv.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 13:22:07 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 13:42:49 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv

# 1 way (printing argv[0])
for i in range(len(argv)):
	print(argv[i])

# 2 way
for i in range(1,len(argv)):
	print(argv[i])

# 3 way (printing argv[0])
for arg in argv:
	print(arg)
