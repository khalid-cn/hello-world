from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello World"
@app.route('/gcd/', METHOD=['POST'])
def gcd(a, b):
    req_data = request.get_json()
    a = req_data["a"]
    b = req_data["b"]
    g = 1
    if(not (isinstance(a, int) and isinstance(b, int))):
        return "Invalid Input - Inputs are not integers"
    elif(a == 0 or b == 0):
        return "Invalid Input - one of the numbers is zero"    
    if( a < b):
        c = a
        a = b
        b = c
    if(a%b == 0):
        g = b
    else:
        while(b > 0) :
            a = a%b
            c = a
            a = b
            b = c  
        g = a
    return '''the gcd of {} and {} is {}'''.format(req_data["a"], req_data["b"], g)

if __name__ == '__main__':
    app.run(port=8080)