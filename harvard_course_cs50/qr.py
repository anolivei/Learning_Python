# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    qr.py                                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/09 23:07:11 by anolivei          #+#    #+#              #
#    Updated: 2021/06/09 23:07:14 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import qrcode

image = qrcode.make("https://www.youtube.com/watch?v=G1IbRujko-A")
image.save("qr.png", "PNG")