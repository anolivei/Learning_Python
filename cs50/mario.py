# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mario.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 17:18:50 by anolivei          #+#    #+#              #
#    Updated: 2021/06/07 17:30:54 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 1
for i in range(4):
	print("?", end="")
print()

print()

# 2
print("?" * 4)

print()

# 3
for i in range(3):
	print("#")

print()

# 4
print("#\n" * 3, end="")

print()

# 5
for i in range(3):
	for j in range(3):
		print("#", end="")
	print()

print()

# 6
for i in range(3):
	print("#" * 3)