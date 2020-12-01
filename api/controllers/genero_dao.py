from flask import jsonify, make_response
from ..models.genero import Genero, GeneroSchema
from .. import db

class GeneroDAO():
    def add(self, data):
        """
            Insert data into table genero
        """
        try:
            obj = Genero()
            obj.name = data.get('name')

            db.session.add(obj)
            db.session.commit()

            return make_response(
                jsonify({
                    'message': 'Added successfully.'
                }, 200)
            )
        except Exception as err:
            return make_response(
                jsonify({
                    'error': '{0}'.format(err)
                }, 406)
            )

    def get_by_id(self, id):
        """
            Get genero data refereced by id
        """
        return GeneroSchema().dump(Genero.query.filter(Genero.id==id).one())