from bottle import route, run


@route("/")
def hello():
    res = '<h2>target website</h2>'
    res += '<button type="button" value="button"'
    res += 'onclick="alert(\'商品を購入しました\')">'
    res += '商品Aを購入する</button>'
    return res


if __name__ == "__main__":
    run(host="0.0.0.0", port=8000, debug=True)
