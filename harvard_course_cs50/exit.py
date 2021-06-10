# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exit.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 13:54:28 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 13:58:06 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import argv, exit

if len(argv) != 2:
	print("missing command-line argument")
	exit(1)
print("Hello, {}".format(argv[1]))
exit(0)