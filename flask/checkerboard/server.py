from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", x=8, y=8)

@app.route('/<int:y>')
def row_y(y):
    return render_template("index.html", x=8, y=y)

@app.route('/<int:x>/<int:y>')  
def custom_xy(x, y):
    return render_template("index.html", x=x, y=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def custom_xy_colors(x, y, color1, color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)
