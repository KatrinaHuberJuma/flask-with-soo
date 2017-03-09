from random import choice, sample

from flask import Flask, render_template, request, session


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():

    user_answer = request.args.get('playing')

    if user_answer == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")




@app.route('/madlib')
def run_madlib():

    colors = request.args.getlist('colors')
    noun = request.args.get('noun')
    person = request.args.get('person')
    adjective = request.args.get('adjective')

    rand_endpoint = choice(["madlibs"])
    # receive it and use the madlib.html to print it
    return render_template(rand_endpoint + '.html', colors=colors,noun=noun,person=person,adjective=adjective)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
