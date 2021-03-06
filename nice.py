from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return '<a href="/hello">Take me to hello.</a>'

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>

            <br>

            <form action="/greet" method="POST">
                <label>What's your name? <input type="text" name="person"></label>
                <br><br>
                <label>Please select a compliment:
                <select name="compliment-type">
                    <option value="awesome">Awesome</option>
                    <option value="fantabulous">Fantabulous</option>
                    <option value="fly">Fly</option>
                    <option value="coolio">Coolio</option>
                    <option value="bitchin">Bitchin</option> <!-- does not update with debug=False -->
                </select></label><br><br>
                <input type="submit" value="Compliment Me!">
            </form>
            <br><br><br>
            
            <form action="/diss" method="POST">
                <label>What's your name? <input type="text" name="person"></label>
                <br><br>
                <label>Please select a diss:
                <select name="diss-type">
                    <option value="a buttface">A Buttface</option>
                    <option value="not fantabulous">Not Fantabulous</option>
                    <option value="smelly">Smelly</option>
                    <option value="a disease">A Disease</option>
                    <option value="smelly in spirit">Smelly, in Spirit</option> <!-- does not update with debug=False -->
                </select></label><br><br>
                <input type="submit" value="Diss Me!">
            </form>
        </body>
    </html>

    """

@app.route('/greet', methods=["POST"])
def greet_person():
    player = request.form.get("person")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

    compliment = request.form.get("compliment-type")
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)

@app.route('/diss', methods=["POST"])
def diss_person():
    player = request.form.get("person")
    diss = request.form.get("diss-type")
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>A Diss</title>
    </head>
    <body>
        Hi {}, I think you're {}!
    </body>
    </html""".format(player, diss)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True) # need to restart server when switching from false to true
