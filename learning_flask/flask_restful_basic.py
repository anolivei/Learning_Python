# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    flask_restful_basic.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/17 23:57:17 by anolivei          #+#    #+#              #
#    Updated: 2021/05/22 11:28:24 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class hello_world(Resource):
	def get(self):
		return {"about": "Hello World!"}

	def post(self):
		some_json = request.get_json()
		return {'you sent': some_json}, 201

class multi(Resource):
	def get(self, num):
		return {'result': num*10}

api.add_resource(hello_world, '/')
api.add_resource(multi, '/multi/<int:num>')

if __name__ == '__main__':
	app.run(debug=True)
