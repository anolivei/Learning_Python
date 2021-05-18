# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    flask_excel.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/05/18 01:07:45 by anolivei          #+#    #+#              #
#    Updated: 2021/05/18 01:37:52 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/data', methods = ['GET', 'POST'])
def data():
	if request.method == 'POST':
		file = request.form['upload-file']
		data = pd.read_csv(file)
		return render_template('data.html', data = data.to_html())

if __name__ == '__main__':
	app.run(debug=True)