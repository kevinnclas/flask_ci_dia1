# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:33:18 2020

@author: kevin
"""
from flask import Flask
from redis import Redis, RedisError

#create a dis instance
redis = Redis(host="redis-server", db=0)

#create a flask application instance
app = Flask(__name__)

#define my own routes

@app.route('/')
def hello():
	return "<h1> Hello World ! </h1>"

@app.route('/visit')
def incr_counter():
	try:
		visits = redis.incr("counter")
	except:
		visits = "<i> I could not connect to the redis server </i>"
	html = "<h1> Number of visits : {}</h1>".format(visits)
	return html

if __name__ == "__main__":
	app.run(debug=True, port=80, host="0.0.0.0")