from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '123abc'

class DataCollectionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    grades = TextAreaField('Grades', validators=[DataRequired()])
    satisfaction = SelectField('Satisfaction', choices=[
        ('very_satisfied', 'Very Satisfied'),
        ('satisfied', 'Satisfied'),
        ('neutral', 'Neutral'),
        ('dissatisfied', 'Dissatisfied'),
        ('very_dissatisfied', 'Very Dissatisfied')
    ])
    suggestions = TextAreaField('Suggestions')
    submit = SubmitField('Submit')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/information')
def information():
    return render_template('information.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()
    if form.validate_on_submit():
        # Save data to .txt file or process it
        return 'Form submitted'
    return render_template('data_collection.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
