# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 21:39:15 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 21:39:32 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import qrcode

image = qrcode.make("https://www.youtube.com/watch?v=G1IbRujko-A")
image.save("qr.png", "PNG")