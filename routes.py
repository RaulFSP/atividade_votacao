
from app import app, db
from flask import Flask, render_template, flash, redirect, url_for, request
from forms import CandidatoForm
from models import Candidato


@app.route("/")
def index():
    try:
        candidatos = db.session.execute(db.select(Candidato)).scalars()
        return render_template("index.html",candidatos=candidatos)
    except Exception as e:
        return "Houve um erro com o index\n"+str(e)





@app.route("/adicionar_candidato", methods=['POST','GET'])
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
def alterar_candidato(id):
    form = CandidatoForm()
    candidato = Candidato.query.get_or_404(id)
    form.nome.data = candidato.nome
    form.cpf.data = candidato.cpf
    if form.validate_on_submit():
        candidato.nome = form.nome.data
        candidato.cpf = form.cpf.data
        try:
            db.session.commit()
        except Exception as e:
            return "Erro na alteração de candidato!\n".format(str(e))
        flash(f"Candidato '{form.nome.data}' alterado!")
        return redirect(url_for('adicionar_candidato'))
    
    return render_template('alterar_candidato.html',form=form, candidato=candidato)
    
        

    


@app.route("/deletar_candidato/<int:id>", methods=['POST','GET'])
def deletar_candidato(id):
    try:
        candidato = db.get_or_404(Candidato,id)
        db.session.delete(candidato)
        db.session.commit()
        flash(f"O candidato '{candidato.nome}' foi removido!")
        return redirect(url_for('adicionar_candidato'))
    except Exception as e:
        return "Erro na exclusão de candidato!\n".format(str(e))