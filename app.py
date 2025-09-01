from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO WORLD!!'

@app.route('/hello1')
def hello():
    return 'hello1'

@app.route("/hello2")
def hello2():
    return 'hello2'

@app.route("/test")

def test():
    a=1+93
    return "addition {}".format(a)
#to get input url
@app.route("/data")
def data():
    data=request.args.get("q")
    return 'this is data from url given by {}'.format(data)


if __name__=="__main__":
    app.run(debug=True)