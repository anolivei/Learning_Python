# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    phonebook_file.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 16:58:51 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 17:20:50 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv
from cs50 import get_string


name = get_string("Name: ")
number = get_string("Number: ")

# 1 way
'''
file = open("phonebook.csv", "a")
writer = csv.writer(file)
writer.writerow((name, number))
file.close()
'''
# 2 way
with open("phonebook.csv", "a") as file:
	writer = csv.writer(file)
	writer.writerow((name, number))