from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PropertyForm(FlaskForm):
	Title = TextField("Property Title", validators=[DataRequired()])
	details = TextAreaField("Description", validators=[DataRequired()], render_kw={"rows": 5, "cols": 60})
	spaces = TextField("Number of Rooms", validators=[DataRequired()])
	bathroom = TextField("Number of Bathrooms", validators=[DataRequired()])
	cost = TextField("Cost", validators=[DataRequired()])
	located = TextField("Location", validators=[DataRequired()])
	prop_type = SelectField(u'Property Type', choices=[('House'), ('Apartment')])
	photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])
