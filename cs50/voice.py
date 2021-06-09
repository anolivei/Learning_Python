# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    voice.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 19:37:56 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 21:30:15 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import speech_recognition
import re

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
	print("Say something!")
	audio = recognizer.listen(source)
words = recognizer.recognize_google(audio)
maches = re.search("my name is (.*)", words)
if maches:
	print("Hey, {}".format(maches[1]))
elif "hello" in words:
	print("Hello to you too!")
elif "how are you" in words:
	print("I am fine, thanks!")
elif "bye" in words:
	print("Goodbye to you too!")
elif "I love you" in words:
	print("Thank you.")
else:
	print("There is any if else for this")