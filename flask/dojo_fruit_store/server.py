from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    strawberry = request.form.get('strawberry', 0)
    raspberry = request.form.get('raspberry', 0)
    apple = request.form.get('apple', 0)
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    student_id = request.form.get('student_id')

    count = int(strawberry) + int(raspberry) + int(apple)
    print(f"Charging {first_name} {last_name} for {count} fruits.")
    
    now = datetime.now().strftime("%B %d %Y %I:%M:%S %p")

    return render_template("checkout.html",
                           strawberry=strawberry,
                           raspberry=raspberry,
                           apple=apple,
                           first_name=first_name,
                           last_name=last_name,
                           student_id=student_id,
                           count=count,
                           now=now)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    