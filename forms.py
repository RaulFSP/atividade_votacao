from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length


class CandidatoForm(FlaskForm):
    nome = StringField(label="Nome do Candidato",validators=[DataRequired(), Length(0,100)])
    cpf = StringField(label="CPF",validators=[DataRequired(),Length(11,11)])
    submit = SubmitField()

