from .. import db, ma

class Filme(db.Model):
    __tableName__ = 'filme'

    id = db.Column(db.Integer,primary_key=True, server_default=db.FetchedValue())
    titulo = db.Column(db.String(120))
    ano = db.Column(db.String(4))
    id_genero = db.Column(db.ForeignKey('genero.id'), nullable=False)

    tb_genero = db.relationship('Genero', primaryjoin='Filme.id_genero == Genero.id', backref='genero')

class FilmeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'titulo', 'ano', 'id_genero')