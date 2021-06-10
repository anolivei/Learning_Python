# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    phonebook.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 14:50:46 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 15:17:14 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import exit
from sys import argv

people = {
	"EMMA" : "11999606020",
	"ANA" : "11998506021",
	"GEORGE" : "11996666021",
	"HERBERT" : "11999955663"
}
if len(argv) != 2:
	print("missing command-line argument")
	exit(1)
if argv[1].upper() in people:
	print("Found\nPhone Number: {}".format(people[argv[1].upper()]))
	exit(0)
print("Not Found")
exit(1)