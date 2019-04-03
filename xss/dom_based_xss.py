from bottle import route,run,request

@route('/')
def hello(user=""):
	username=request.query.get("user")
	username='' if username is None else usename

	res="<h2>hello</h2>"
	script="<script>"
	script+="document.write( unescape('URL ' +  document.baseURI) )"
	script+='</script>'
	print(res+script)
	return  res + script

if __name__=="__main__":
	run(host="0.0.0.0",port=8080,debug=True)