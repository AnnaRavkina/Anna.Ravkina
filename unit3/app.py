from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The Golden Fish"
    
    text = """It's 5 am, you're sleepy and fishing in the local lake hoping to catch some fish for lunch. Finally you catch a goldfish and start picturing how you're going to fry it. However, a fish starts talking to you like a human: "Hey, I'm a magical fish, please, let me go and I'll make your wish come true!". You're shocked."""

    choices = [
        ('talk',"Respond to the fish"),
        ('let_go',"You must have gotten a sunstoke! Let the fish go and leave.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/wish")
def talk():
    title = "Respond to the fish"
    
    text = """You ask the fish about it's magic. It tells you to make a wish and see it yourself."""

    choices = [
        ('make_wish',"Make a wish!"),
        ('let_go',"You think you've gone crazy and let the fish go.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/let_go")
def let_go():
    title = "You must have gotten a sunstoke! You let the fish go and leave."
    
    text = """You free the fish and run back home thinking you should book a session with a therapist."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/end")
def make_wish():
    title = "Make a wish!"
    
    text = """You close your eyes and make a wish. A red Lamborghini appears. "You're pathetic," - the fish says. You feel assaulted, but let it go immediately and drive back home."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
