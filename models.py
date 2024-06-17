from datetime import datetime, timezone
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey
from datetime import datetime, timezone
from app import app,db

class Candidato(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    cpf = mapped_column(String(11), nullable=False)

class Eleitor(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    cpf = mapped_column(String(11), nullable=False)

class Voto(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    cpf_candidato = mapped_column(Integer, ForeignKey(Candidato.id), nullable=False)
    data_voto = mapped_column(DateTime, default=datetime.now(timezone.utc))
