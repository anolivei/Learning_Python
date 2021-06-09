# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    agree.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/06 21:23:51 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 19:08:59 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cs50 import get_string
import re

s = get_string("Do you agree?\n")

# 1 way
''' 
if (s == "y" or s == "Y"):
	print("Agreed.")
elif (s == "n" or s == "N"):
	print("Not agreed.")
else:
	print("Invalid string.")
'''
# 2 way
'''
if (s in ["y", "Y"]):
	print("Agreed.")
elif (s in ["n", "N"]):
	print("Not agreed.")
else:
	print("Invalid string.")
'''
# 3 way
'''
if (s.lower() in ["y", "yes"]):
	print("Agreed.")
elif (s.lower() in ["n", "no"]):
	print("Not agreed.")
else:
	print("Invalid string.")
'''
# 4 way
'''
if re.search("yes|y", s):
	print("Agreed.")
elif re.search("no|n", s):
	print("Not agreed.")
else:
	print("Invalid string.")'
'''
# 5 way
if re.search("^y(es)?$", s, re.IGNORECASE):
	print("Agreed.")
elif re.search("^n(o)?$", s, re.IGNORECASE):
	print("Not agreed.")
else:
	print("Invalid string.")