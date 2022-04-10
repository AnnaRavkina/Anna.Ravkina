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

@app.route('/dictionary/<string:word>')
def dictionary(word):
    title = "Dictionary"
    f = open('words.txt')
    word_list = f.read().splitlines()
    word = word.lower()
    l = []
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
    isreal = True

    for item in word_list:
        item = item.lower()
        if item == word:
            for letter in letters:
                l.append(item + letter)
    if l == []:
        isreal = False
    else:
        isreal = True
    return render_template('dictionary.html', title = title, words=l, isreal=isreal, original=word)


