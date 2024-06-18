from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField
from wtforms.validators import DataRequired, Length


class CandidatoForm(FlaskForm):
    nome = StringField(label="Nome do Candidato",validators=[DataRequired(), Length(3,100)])
    cpf = StringField(label="CPF",validators=[DataRequired(),Length(11,11)])
    img = FileField("Adicione uma Imagem", validators=[DataRequired()])
    submit = SubmitField()

class UsuarioForm(FlaskForm):
    nome = StringField(label="Nome Completo", validators=[DataRequired(), Length(3,100)])
    username = StringField(label="Username", validators=[DataRequired(), Length(1,30)])
    cpf = StringField(label="CPF",validators=[DataRequired(),Length(11,11)])
    email = StringField(label="Email",validators=[DataRequired(),Length(1,100)])
    password = PasswordField(label="Senha",validators=[DataRequired(),Length(3,20)])
    submit = SubmitField()

class EleitorForm(FlaskForm):
    cpf = StringField(label="CPF",validators=[DataRequired(),Length(11,11)])
    submit = SubmitField()




class UsuarioLoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(3,100)])
    password = PasswordField(label="Senha",validators=[DataRequired(),Length(3,20)])
    submit = SubmitField()