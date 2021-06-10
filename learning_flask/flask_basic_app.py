# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    flask_basic_app.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/17 23:24:08 by anolivei          #+#    #+#              #
#    Updated: 2021/05/17 23:38:50 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		some_json = request.get_json()
		return jsonify({'you sent': some_json}), 201
	else:
		return jsonify({"about": "Hello World!"})

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
	return jsonify({'result': num*10})

if __name__ == '__main__':
	app.run(debug=True)
