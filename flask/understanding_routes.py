from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # application type json
    return "hellp world"  
  
@app.route('/say/<name>')
def say_hello(name):
    return f"Hi {name}"  

@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return word * num

if __name__ == '__main__':
    app.run(debug=True)