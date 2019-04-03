from bottle import route,run

@route("/")
def hello():
	target_url="http://localhost:8000"
	out='<h2>攻撃用</h2>'
	out+='<iframe src="{}" ></iframe>'.format(target_url)#, **kwargs)
	return out

if __name__=="__main__":
	run(host="0.0.0.0",port=8080,debug=True)