'''
from flask import Flask, request,render_template,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods = ['POST'])
def math_operation():
    
    if request.method == 'POST':
        op = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
    try:
        if op == 'add':
            r = num1 + num2
            result = "The Sum of "+ str(num1) +" and "+ str(num2) +" is "+str(r)
        
            return render_template('results.html',result = result)

        if op == 'subtract':
            r = num1 - num2
            result = "The Subtraction of "+ str(num1) +" and "+ str(num2) +" is "+str(r)
        
            return render_template('results.html',result = result)

        if op == 'multiply':
            r = num1 * num2
            result = "The Multiplication of "+ str(num1) +" and "+ str(num2) +" is "+str(r)
        
            return render_template('results.html',result = result)

        if op == 'divide':
            r = num1 / num2
            result = "The Division of "+ str(num1) +" and "+ str(num2) +" is "+str(r)
        
            return render_template('results.html',result = result)

    except Exception as e:
        er = "ERROR OCCURED :"+str(e)+"\nNOTE: Please Enter Correct Numbers"
        return render_template('results.html',result = er)
'''

from flask import Flask, request,render_template,jsonify

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/postman_data',methods = ['POST'])
def math_operation():

    if request.method == 'POST':
        op = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
    try:
        if op == 'add':
            r = num1 + num2
            result = "The Sum of "+ str(num1) +" and "+ str(num2) +" is "+str(r)

        if op == 'subtract':
            r = num1 - num2
            result = "The Subtraction of "+ str(num1) +" and "+ str(num2) +" is "+str(r)
        
            
        if op == 'multiply':
            r = num1 * num2
            result = "The Multiplication of "+ str(num1) +" and "+ str(num2) +" is "+str(r)
        
            
        if op == 'divide':
            r = num1 / num2
            result = "The Division of "+ str(num1) +" and "+ str(num2) +" is "+str(r)
        
        return jsonify(result)

    except Exception as e:
        er = "ERROR OCCURED : "+str(e)+"NOTE: Please Enter Correct Numbers"
        return render_template('results.html',result = er)





if __name__=="__main__":
    app.run(host="0.0.0.0")
