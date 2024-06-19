SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(
    "mysql+pymysql",
    "root",
    "1234",
    "localhost",
    "3306",
    "atividade_votacao"
)

SECRET_KEY = "banan4"