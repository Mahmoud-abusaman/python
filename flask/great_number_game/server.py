import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'super_secret_game_key'

@app.route('/')
def index():
    if 'target_num' not in session:
        session['target_num'] = random.randint(1, 100)
    
    guess_status = session.get('guess_status', None)
    
    return render_template('index.html', status=guess_status)

@app.route('/guess', methods=['POST'])
def process_guess():
    if 'guess' in request.form and request.form['guess'].isdigit():
        user_guess = int(request.form['guess'])
        target = session['target_num']

        if user_guess > target:
            session['guess_status'] = 'high'
        elif user_guess < target:
            session['guess_status'] = 'low'
        else:
            session['guess_status'] = 'correct'
            
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('target_num', None)
    session.pop('guess_status', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)