from flask import Flask, request, render_template, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'mykey'

@app.route('/', methods=['get','post'])
def njgld():
    session['log'] = []
    session['state'] = None
    session['time'] = None
    session['gold'] = 0
    session['delta'] = 0
    session['building']= None
    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def guess():
    session['state'] = 'process_money'
    if request.form['building'] == 'farm':
        session['delta'] = random.randint(10,20)
        session['gold'] += session['delta']
        session['building'] = 'farm'
    elif request.form['building'] == 'cave':
        session['delta'] = random.randint(5,10)
        session['gold'] += session['delta']
        session['building'] = 'cave'
    elif request.form['building'] == 'house':
        session['delta'] = random.randint(2,5)
        session['gold'] += session['delta']
        session['building'] = 'house'
    elif request.form['building'] == 'casino':
        session['delta'] = random.randint(-50,50)
        session['gold'] += session['delta']
        session['building'] = 'casino'
    session['time'] = datetime.now()
    session['log'].append((session['building'],session['delta'],session['time']))
    return render_template('index.html')

@app.route('/reset', methods=['post'])
def reset():
    session['log'] = []
    session['state'] = None
    session['building'] = None
    session['gold'] = 0
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
