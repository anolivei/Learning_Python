# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    cough.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/07 14:38:20 by anolivei          #+#    #+#              #
#    Updated: 2021/06/07 17:16:02 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# 1 way (simple)
for i in range(3):
	print("cough")

# 2 way (with functions)

def	main():
	cough(3)

def cough(n):
	for i in range(n):
		print("cough")

main()

# 3 way (pythonic way)
print("cough\n" * 2 + "cough")

# 4 way (more pythonic way)
print("cough\n" * 3, end="")