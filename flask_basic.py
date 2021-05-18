# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    flask_basic.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/17 22:54:42 by anolivei          #+#    #+#              #
#    Updated: 2021/05/17 22:56:04 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
	return jsonify({"about": "Hello, World!\n"})

if __name__ == '__main__':
	app.run(debug=True)