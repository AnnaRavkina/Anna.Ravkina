from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    title = "This is a FizzBuzz Web App"
    return render_template('main.html', title=title)

@app.route('/fizzbuzz/<int:do_challenge>')
def fizzbuzz(do_challenge):
    l = []
    i = 1
    while i <= do_challenge:
        l.append(i)
        i += 1
    if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
    elif i % 3 == 0:
            print('Fizz')
    elif i % 5 == 0:
            print('Buzz')
    else: 
            print(i)
    
    return render_template('fizzbuzz.html', do_challenge=do_challenge, numbers=l)

