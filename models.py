from datetime import datetime, timezone
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.mysql import LONGBLOB
from datetime import datetime, timezone
from app import app,db
from flask_login import UserMixin

class Candidato(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    cpf = mapped_column(String(11), nullable=False, unique=True)
    img = mapped_column(LONGBLOB, nullable=False)
    img_name = mapped_column(Text, nullable=False)

class Eleitor(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    cpf = mapped_column(String(11), nullable=False, unique=True)

class Voto(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_candidato = mapped_column(Integer, ForeignKey(Candidato.id))
    data_voto = mapped_column(DateTime, default=datetime.now(timezone.utc))

class Usuario(db.Model, UserMixin):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome = mapped_column(String(100), nullable=False)
    cpf = mapped_column(String(11), nullable=False, unique=True)
    username = mapped_column(String(30), nullable=False, unique=True)
    email = mapped_column(String(100), nullable=False)
    password = mapped_column(String(20), nullable=False)
