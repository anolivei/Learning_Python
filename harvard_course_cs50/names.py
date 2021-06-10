# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    names.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 14:34:00 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 14:41:56 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import exit
from sys import argv

names = ["ANA", "PEDRO", "MARIA", "DAVID"]

#1 way
'''
if "ANA" in names:
	print("Found")
	exit(0)
print("Not found")
exit(1)
'''

# 2 way
if len(argv) != 2:
	print("missing command-line argument")
	exit(1)
if argv[1].upper() in names:
	print("Found")
	exit(0)
print("Not found")
exit(1)