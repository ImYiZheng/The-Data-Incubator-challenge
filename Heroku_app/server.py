import os
from flask import Flask,render_template,request,redirect
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/plot1',methods=['POST'])
def plot1():
    return render_template('plot1.html')

@app.route('/plot2',methods=['POST'])
def plot2():
    return render_template('plot2.html')

@app.route('/home',methods=['POST'])
def next_():
    return redirect('/')



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
