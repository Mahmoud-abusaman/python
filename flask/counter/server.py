from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1

    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)