from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def anagram():
    title = "This is an Anagrams web page"
    return render_template('main.html', title=title)

@app.route('/words/<string:anagram>')
def words(anagram):
    title = "These are the anagrams for your word:"
    f = open('words.txt')

    word_list = f.read().splitlines()

    anagram = anagram.lower()
    l = []

    for word in word_list:
        word = word.lower()
        if len(word) == len(anagram) and sorted(word) == sorted(anagram) and word != anagram:
            l.append(word)

    return render_template('second.html', title=title, words=l)



