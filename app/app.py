import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

foodtypes = []
locations = []
prices = []

@app.route('/')
def index():
    del foodtypes[:]
    del locations[:]
    del prices[:]
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/nextperson', methods = ['POST'])
def nextperson():
    foodtypes.append(request.form['foodtype'])
    locations.append(request.form['location'])
    prices.append(request.form['price'])
    print(foodtypes)
    print(locations)
    print(prices)
    if request.form['submit'] == "Add another person!":
        return redirect('/search')
    elif request.form['submit'] == "Find me a restaurant!":
        return redirect('/results')


@app.route('/getstarted', methods = ['POST'])
def getstarted():
    return redirect('/search')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__=="__main__":
    app.debug = True
    app.run()