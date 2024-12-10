#让我们的电脑可以支持服务访问
#需要一个web框架
#pip install flask
from flask import Flask,render_template
#创建一个web应用
app = Flask(__name__) 

hero = [
'黑暗之女','狂战士','正义巨像','卡牌大师','德邦总管','无畏战车','诡术妖姬'
,'正义天使','牛头酋长','无极剑圣']


@app.route('/index')#设置了一个路线\
def index():
    return render_template('index.html')

app.run(debug=True)
#方便以后改代码不需要反复的重启应用


#http://127.0.0.1(电脑):5000（服务）/index（）