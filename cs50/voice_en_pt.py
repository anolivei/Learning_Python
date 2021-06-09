# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    voice.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/06/08 19:17:48 by anolivei          #+#    #+#              #
#    Updated: 2021/06/08 21:09:36 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sys import exit
import speech_recognition
from cs50 import get_string

print("Choose you language")
n = get_string("Type P to Portuguese or E to English: ").upper()
if n == "P":
	lan = "pt-BR"
elif n == "E":
	lan = "en-US"
else:
	print("Invalid language.")
	exit(1)
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
	print("Say something!")
	audio = recognizer.listen(source)
print("Google Speech Recognition thinks you said:")
print(recognizer.recognize_google(audio, language = lan))
exit(0)
