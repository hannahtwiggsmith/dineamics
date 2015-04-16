import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

foodtypes = []
locations = []
prices = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/nextperson', methods = ['POST'])
def nextperson():
    foodtype = request.form['foodtype']
    foodtypes.append(foodtype)
    location = request.form['location']
    locations.append(location)
    price = request.form['price']
    prices.append(price)
    print(foodtypes)
    print(locations)
    print(prices)
    if request.form['btn1'] == "Add another person!":
    	return redirect('/search')
    else:
    	return redirect('/results')

# @app.route('/finish', methods = ['POST'])
# def finish():
#     return redirect('/results')	

@app.route('/getstarted', methods = ['POST'])
def getstarted():
    return redirect('/search')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__=="__main__":    
    app.debug = True
    app.run()