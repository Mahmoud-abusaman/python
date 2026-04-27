from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # application type json
    return {'message': 'Hello, World!', 'status': 'success', 'data': {'key': 'value', 'number': 42}}   
  
if __name__ == '__main__':
    app.run(debug=True)