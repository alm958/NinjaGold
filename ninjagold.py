from flask import Flask, request, render_template, redirect, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'mykey'

// Is 'post' nessesary for this route?
@app.route('/', methods=['get','post'])
def njgld():
    // Comments: There is alot of use of session for holding variable data globaly that isn't nessesary. Should think about session as a
    // a variable space that can be accessed from other pages and will retain it's data regardless of what file you are accessing. If you
    // do not need to do a running save of date (You do for gold and log so these are good) then you should probably use local variables instead. (time, building and delta could all have been done using local variables.
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
    // Any time you have more than one route rendering the same template, you should stop and think if this is nessesary. In this case, the thought process is that when you are done with the code above, you will then redirect to '/' in order to render your index HTML. The same will hold true for your '/reset' route.
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
