# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import  PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import  DataRequired, Email, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Laboratorio, Usuario

class LabortorioForm(FlaskForm):
    """
	Form para adicionar Laboratório
	"""
    descricao = StringField('Descrição', validators=[DataRequired()])
    professorTitular = QuerySelectField(validators=[DataRequired()], query_factory=lambda: Usuario.query.all(), get_label="nome") 
    professorSuplente = QuerySelectField(validators=[DataRequired()], query_factory=lambda: Usuario.query.all(), get_label="nome") 
    submit = SubmitField('Adicionar')

    def validate_descricao(self, field):
		if Laboratorio.query.filter_by(descricao=field.data).first():
			raise ValidationError('Laboratório com mesma descrição já criado.')
        
    def validate_professorSuplente(self, field):
        if field.data == self.professorTitular.data:
            raise ValidationError("O professor Suplente deve ser diferente do Titular!")
            