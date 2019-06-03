from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed   # for images uplading
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app_files.db_models import User, Item

#------------------------------ REGISTRATION FORM ----------------------------------#
class RegistrationForm(FlaskForm):
	username = StringField('Nombres',
							validators=[DataRequired("Colocar nombres"),
							Length(min=2, max=20, message="Debe contener como minimo %(min)d do %(max)d caracteres")])
	email = StringField('Email',
						validators=[DataRequired("Campo obligatorio"),
						Email("Direccion de email")])
	password = PasswordField('Contraseña', validators=[DataRequired("Campo obligatorio")])
	confirmPassword = PasswordField('Confirmar contraseña',
									 validators=[DataRequired("Campo obligatorio"),
									 EqualTo('password', message="Las contraseñas no coinciden")])
	submit = SubmitField('Crear una cuenta')

	# custom validation - checks if the given value is uniqe
	# no need to call this function - FlaskForm class makes it automatically
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first() # returns None if it doesn`t exist
		if user:
			raise ValidationError("El nombre de usuario ya está tomado")

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first() # returns None if it doesn`t exist
		if email:
			raise ValidationError("Ya existe una cuenta con la dirección de correo electrónico proporcionada.")


#---------------------------------- LOGIN FORM -------------------------------------#

class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Contraseña', validators=[DataRequired("Campo obligatorio")])
	remember = BooleanField('Recuerdame')
	submit = SubmitField('Acceder')

#------------------------------ ORDER STATUS FORM ----------------------------------#

class OrderStatusForm(FlaskForm):
	status = RadioField('Aktualizuj status', choices=[('W trakcie realizacji', 'W trakcie realizacji'),
		('Wysłano', "Wysłano"), ('Dostarczono', 'Dostarczono')])
	orderID = StringField('Nr zamówienia')
	submit = SubmitField('Zaktualizuj')


#-------------------------------- NEW ITEM FORM ------------------------------------#


