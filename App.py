import flask
import flask_wtf
import wtforms

# made flask application with custom name
app = flask.Flask("My project")
# made a key for the app which is needed to work with forms
app.config["SECRET_KEY"] = "password"

# added route for welcome page (this will also be the first page to open when App.py runs
@app.route("/")
def welcome_page():
    # renders and returns the welcome html page
    return flask.render_template("welcome_page.html")

@app.route("/information_page")
def information_page():
    return flask.render_template("information_page.html")