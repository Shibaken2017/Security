from bottle import route,run,request,response,redirect,get
import os
import sys,random
import secrets

USER_ID="user1"
os.environ["PASSWORD"]='123456'
token=""

def valideate_token():
	return token==request.forms.get('token')

def gen_token():
	return secrets.token_urlsafe()

@route("/")
def index():
	res="<h2> csrf demo</h2>"
	if isloggedin():
		global token
		if token=="":
			token=gen_token()
		hidden_form='<input type="hidden" name="token" value="{}">'.format(token)#*args, **kwargs
		username=request.get_cookie('session_id',secret='password')
		res+='<form action="/changepasswd" method="POST">'
		res+='change password: <input type="text" name="password" />'
		res+=hidden_form
		res+='<input type="submit" value="update">'
		res+='</form>'

		return res +'helloo'+ str(username)#object
	else:
		return res +'you must login <a href="/login">here</a>'

@route('/changepasswd',method="POST")
def change_passwd():
	if not valideate_token():
		return 'your token is invalid'
	if isloggedin():
		new=request.forms.get("password")
		os.environ["PASSWORD"]=new

		return redirect("/login")
	else:
		return 'you must loin <a href="/login">here</a>'




@route("/login")
def login():
	res='<h2>csrf demo</h2>'
	res+='<form action="/login", method="POST">'
	res+='USER ID: <input type="text" name="user_id"/><br>'
	res+='password: <input type="text" name="password"/>'
	res+='<input type="submit" value="login"/>'
	res+='</form>'

	return res

@route("/login",method="POST")
def do_login():
	user_id=request.forms.get("user_id")
	password=request.forms.get("password")
	if authenticate(user_id,password):
		response.set_cookie("session_id",user_id,secret="password")
		return redirect("/")
	else:
		return "<h2>csrf demo</h2>login failed"


def isloggedin():
	cookie=request.get_cookie('session_id',secret='password')
	print(cookie)
	return False if cookie is None else True

def authenticate(user_id,password):
	print(os.environ["PASSWORD"])
	print(user_id)#)
	print(password)#value
	if user_id ==USER_ID and password==os.environ["PASSWORD"]:
		return True
	else:
		return False
if __name__=="__main__":
	run(host="0.0.0.0",port=8000,debug=True)