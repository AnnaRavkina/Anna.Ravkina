from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    title = "This is a FizzBuzz Web App"
    return render_template('main.html', title=title)

@app.route('/fizzbuzz/<int:do_challenge>')
def fizzbuzz(do_challenge):
        l = []

        for i in range(0, do_challenge):
                if (i % 3 == 0) and (i % 5 == 0):
                        l.append('FizzBuzz')
                elif i % 3 == 0:
                        l.append('Fizz')
                elif i % 5 == 0:
                        l.append('Buzz')
                else: 
                        l.append(i)
        
        return render_template('fizzbuzz.html', numbers=l)

