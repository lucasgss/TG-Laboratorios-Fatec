# -*- coding: utf-8 -*-
from flask import abort, flash, redirect, url_for, render_template
from flask_login import current_user, login_required
from sqlalchemy import or_
from forms import  LabortorioForm
from . import common
from ..models import Laboratorio

from .. import db

def check_admin():
	"""
	Prevent a non admin access
	"""
	if not current_user.is_admin:
		abort(403)

@common.route('/laboratorios')
@login_required
def list_laboratorios():
	"""
	Render the laboratorios template on the /laboratorios route
	"""
	laboratorios = None
	if current_user.is_admin:
		laboratorios = Laboratorio.query.all()
	else:
		laboratorios = Laboratorio.query.filter_by(
			or_(Laboratorio.laboratorio_professorTitular_id == current_user.id, 
			Laboratorio.laboratorio_professorSuplente_id==current_user.id))

	return render_template('common/laboratorios.html', laboratorios=laboratorios, title="Laboratórios").encode('utf-8')
	

@common.route('/laboratorio/adicionar', methods=['GET','POST'])
@login_required
def add_laboratorio():
	"""
	Render the laboratorios template on the /laboratorios route
	"""
	check_admin()
	form = LabortorioForm()
	if form.validate_on_submit():
		laboratorio = Laboratorio(descricao=form.descricao.data,
								professorTitular_id=form.professorTitular_id.data,
								professorSuplente_id=form.professorSuplente_id.data)
		db.session.add(laboratorio)
		db.session.commit()
		flash('Laboratório adicionado com sucesso!')

		# redicreciona para lista de usuarios
		return redirect(url_for('common.list_laboratorios'))

	return render_template('common/laboratorio.html', title="Adicionar Laboratório").encode('utf-8')
	
	
@common.route('/laboratorio/editar/<int:id>', methods=['GET','POST'])
@login_required
def edt_laboratorio(id):
	"""
	Render the laboratorios template on the /laboratorios route
	"""
	check_admin()
	

	return render_template('common/laboratorio.html', title="Adicionar Laboratório").encode('utf-8')
		