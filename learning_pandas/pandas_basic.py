# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pandas_basic.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/18 00:16:14 by anolivei          #+#    #+#              #
#    Updated: 2021/05/18 00:49:52 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

def pandas_basic ():
	df = pd.read_csv("people_data.csv", encoding = "UTF-8", sep = ",", header = 0, usecols = ["nome", "cpf"])
	print(df.head())
	print(df.shape)

if(__name__ == "__main__"):
	pandas_basic()