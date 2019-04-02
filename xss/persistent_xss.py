from bottle import route
from bottle import run
from bottle import request
from bottle import redirect
import sqlite3
import html

db_name="tmp.db"
conn=sqlite3.connect(db_name)
cursor=conn.cursor()

@route("/")
def hello(user=""):
	tasks=get_tasklist()
	res="<h2>Persistent xss demo</h2>"
	res+="<form action='./' method='POST'>"
	res+="task:<input type='text' name='name' /><br>"
	res+="content:<input type='text' name='detail'/><br>"
	res+="<input type='submit' name='register' value='登録'/>"
	res+="</form>"
	res+=tasks
	return res


@route("/", method="POST")
def register():
	name=html.escape(request.forms.get("name"))
	detail=html.escape(request.forms.get("detail"))
	sql_query="insert into tasklist values(?,?)"
	cursor.execute(sql_query,(name,detail))
	conn.commit()
	return redirect("/")

def get_tasklist():
	sql_query='select * from tasklist'
	result=cursor.execute(sql_query)
	res='<table border="1">'
	print(result)#value
	for row in result:
		print(row)#value
		res+="<tr><td>"
		res+=row[0]#.encode("utf-8")
		res+='</td><td>'
		res+=row[1]#.encode("utf-8")
		res+="</td></tr>"
	res+="</table>"
	return res
if __name__=="__main__":
	run(host="0.0.0.0",port=8080,debug=True)