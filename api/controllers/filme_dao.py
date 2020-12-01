from ..models.filme import Filme, FilmeSchema
from .. import db

class FilmeDAO():
    def get_all(self):
        return FilmeSchema().dump(Filme.query.all(), many=True)