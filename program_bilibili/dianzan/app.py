#建立一个服务 需要用一个框架
#pip install flask

from flask import Flask,render_template


app = Flask(__name__)

data = [
    {'id':0,'name':'中秋节','num':0},
    {'id':0,'name':'春节','num':0},
    {'id':0,'name':'建军节','num':0}
]

@app.route('/index')
def index():
    return render_template('index.html',data=data)


app.run(debug=True)