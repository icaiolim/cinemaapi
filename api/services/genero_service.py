from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api
from ..controllers.genero_dao import GeneroDAO as dao

ns = api.namespace('genero','Genero')

@ns.route("/")
class GeneroService(Resource):

    @api.doc(params={'name': 'Nome do gênero a ser adicionado'})
    def post(self):
        ''' Adicionar um novo genero '''
        if self.api.payload is None:
            return make_response(jsonify({'error': 'invalid data'}), 406)
        return dao().add(self.api.payload)


@ns.route("/<id>")
class GeneroServiceItem(Resource):
    def get(self, id):
        ''' Consultar genero por id'''
        return make_response(dao().get_by_id(id), 200)
        


