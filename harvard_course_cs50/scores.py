# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scores.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 01:19:45 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 01:26:07 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
scores = []
scores.append(72)
scores.append(73)
scores.append(33)
'''
scores = [72, 73, 33]

print("Average: {}".format(round(sum(scores) / len(scores), 2)))
print(f"Average: {sum(scores) / len(scores)}")