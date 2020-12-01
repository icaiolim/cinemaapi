from .. import db, ma

class Genero(db.Model):
    __tableName__ = 'genero'

    id = db.Column(db.Integer,primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(60))

class GeneroSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')