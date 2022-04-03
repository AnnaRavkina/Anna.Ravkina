from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def anagram():
    title = "This is an Anagrams web page"
    return render_template('main.html', title=title)

@app.route('/words/<int:anagram>')
def words(anagram):
    title = "These are the anagrams for your word:"
    f = open('words.txt')

    word_list = f.read().splitlines()

    for word in word_list:
        word.upper() == word.lower()


        # I don't think this one is correct, how do I identify other words?
        
        if(len(str(word))) == len(str(word)) and sorted(word) == sorted(word): 
            l = []
            l.append(word)

    return render_template('second.html', title=title, word_list=word_list, anagram=anagram, words=l)