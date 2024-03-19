import flask
import flask_wtf
import wtforms

# made flask application with custom name
app = flask.Flask("My project")
# made a key for the app which is needed to work with forms
app.config["SECRET_KEY"] = "password"

# form to collect data
class DataCollectionForm(flask_wtf.FlaskForm):
    # form fields with validation requirements
    name = wtforms.StringField("Name", validators=[wtforms.validators.DataRequired()])
    student_number = wtforms.StringField("Student number", validators=[wtforms.validators.DataRequired()])
    email = wtforms.EmailField("Email address", validators=[wtforms.validators.DataRequired()])
    grades = wtforms.TextAreaField("Grades obtained in course", validators=[wtforms.validators.DataRequired()])
    satisfaction = wtforms.RadioField("Overall satisfaction with the course",choices=[("very-satisfied","Very satisfied"),("satisfied","Satisfied"),("nuetral","Neutral"),("dissatisfied","Dissatisfied"),("very-dissatisfied","Very dissatisfied")])
    improvement = wtforms.TextAreaField("Suggestions for improvement", validators=[wtforms.validators.DataRequired()])
    submit = wtforms.SubmitField("Submit")


# added route for welcome page (this will also be the first page to open when App.py runs
@app.route("/")
def welcome_page():
    # renders and returns the welcome html page
    return flask.render_template("welcome_page.html")

@app.route("/information_page")
def information_page():
    return flask.render_template("information_page.html")

@app.route("/data_collection", methods=["GET","POST"])
def data_collection():
    form = DataCollectionForm()
    if form.validate_on_submit():
        with open('feedback.txt', 'a') as file:
            file.write(
                f'Name: {form.name.data}, Student number: {form.student_number.data}, Email: {form.email.data}, Grades: {form.grades.data}, Satisfaction: {form.satisfaction.data}, Improvement: {form.improvement.data}\n')
        return flask.redirect(flask.url_for('thank_you'))
    return flask.render_template('data_collection.html', form=form)

@app.route('/thank_you')
def thank_you():
    return flask.render_template('thank_you.html')
app.run()