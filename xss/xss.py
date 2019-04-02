from bottle import route
from bottle import run
from bottle import request
import html
from bottle import response


@route("/")
def hello(user=""):
	username=request.query.get("user")
	username='' if username is None else username
	response.set_header("X-XSS-rotection","1;mode=block")
	response.set_header("Content-Security-Policy","default-src 'self'")

	
	res="<h2>Hello{name}</h2>".format(name=username)#, **kwargs)
	print(res)#value
	return res

if __name__=="__main__":
	run(host="0.0.0.0",port=8080,debug=True)