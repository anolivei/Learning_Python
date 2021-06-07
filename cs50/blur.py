# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    blur.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/05 20:57:24 by anolivei          #+#    #+#              #
#    Updated: 2021/06/06 16:46:48 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PIL import Image, ImageFilter

before = Image.open("test.bmp")
after = before.filter(ImageFilter.BLUR)
after.save("out.bmp")


