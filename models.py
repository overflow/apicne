from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://overflow:137955@localhost/apicne'
db = SQLAlchemy(app)

class Nacional(db.Model):
    __tablename__ = 'nacional'
    nacionalidad = db.Column(db.String(1))
    cedula = db.Column(db.Integer, primary_key=True)
    primer_apellido = db.Column(db.String(100))
    segundo_apellido = db.Column(db.String(100))
    primer_nombre = db.Column(db.String(100))
    segundo_nombre = db.Column(db.String(100))
    cod_centro = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return '{primer_apellido: %s}' % self.primer_apellido

    def as_dict(self):
      return {c.name: getattr(self, c.name) for c in self.__table__.columns}

