
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
        return render_template("adicionar_candidato.html", form=form)