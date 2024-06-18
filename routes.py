from app import app, db, login_manager
from flask import Flask, render_template, flash, redirect, url_for, request
from forms import CandidatoForm, UsuarioForm, UsuarioLoginForm
from models import Candidato, Usuario
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user



# flask login
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get_or_404(id)




# rota index
@app.route("/")
def index():
    try:
        candidatos = db.session.execute(db.select(Candidato)).scalars()
        return render_template("index.html",candidatos=candidatos)
    except Exception as e:
        return "Houve um erro com o index\n"+str(e)




#Rotas de CRUD do Candidato

@app.route("/adicionar_candidato", methods=['POST','GET'])
@login_required
def adicionar_candidato():
    form = CandidatoForm()
    nome = None
    cpf = None
    if form.validate_on_submit():
        nome = form.nome.data
        cpf = form.cpf.data
        try:
            candidato = Candidato(nome=nome,cpf=cpf)
            db.session.add(candidato)
            db.session.commit()
            flash(f"candidato {candidato.nome} Foi adicionado!")
            return redirect(url_for('adicionar_candidato'))
        except Exception as e:
            return "Houve um erro ao adicionar um candidato\n"+str(e)
    else:
        candidatos = db.session.execute(db.select(Candidato)).scalars()
        return render_template("adicionar_candidato.html", form=form, candidatos= candidatos)
    
@app.route("/alterar_candidato/<int:id>", methods=['POST','GET'])
@login_required
def alterar_candidato(id):
    form = CandidatoForm()
    candidato = Candidato.query.get_or_404(id)
    if form.validate_on_submit():
        candidato.nome = form.nome.data
        candidato.cpf = form.cpf.data
        try:
            db.session.commit()
            flash(f"Candidato {candidato.nome} foi alterado!")
            return redirect(url_for("adicionar_candidato"))
        except Exception as e:
            flash("{}".format(str(e)))
            return render_template('alterar_candidato.html',form=form, candidato=candidato)
    else:
        return render_template('alterar_candidato.html',form=form, candidato=candidato)
    
@app.route("/deletar_candidato/<int:id>", methods=['POST','GET'])
@login_required
def deletar_candidato(id):
    try:
        candidato = db.get_or_404(Candidato,id)
        db.session.delete(candidato)
        db.session.commit()
        flash(f"O candidato '{candidato.nome}' foi removido!")
        return redirect(url_for('adicionar_candidato'))
    except Exception as e:
        return "Erro na exclusão de candidato!\n".format(str(e))







#Rotas de CRUD do usuário do sistema

@app.route("/adicionar_usuario", methods=['POST','GET'])
def adicionar_usuario():
    form = UsuarioForm()
    nome = None
    username = None
    cpf = None
    email = None
    password = None
    if form.validate_on_submit():
        nome = form.nome.data
        username = form.username.data
        cpf = form.cpf.data
        email = form.email.data
        password = form.password.data
        try:
            usuario = Usuario(nome=nome,username=username,cpf=cpf,email=email,password=password)
            db.session.add(usuario)
            db.session.commit()
            flash(f"O usuário {usuario.nome} Foi adicionado!")
            return redirect(url_for('adicionar_usuario'))
        except Exception as e:
            return "Houve um erro ao adicionar um usuário\n"+str(e)
    else:
        return render_template("adicionar_usuario.html", form=form)
    







#rota de login do usuário

@app.route('/login', methods=['POST','GET'])
def login():
    form = UsuarioLoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(username=form.username.data).first_or_404()
        if usuario:
            if usuario.password == form.password.data:
                login_user(usuario)
                flash("Logado com sucesso!")
                return redirect(url_for('index'))
            else:
                flash(f"Senha do usuário {usuario.username} está errada!")
        else:
            flash(f"Usuário não existente!")
    else:
        return render_template('login.html', form=form)

@app.route('/logout', methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    flash(f"Deslogado do sistema!")
    return redirect(url_for('index'))