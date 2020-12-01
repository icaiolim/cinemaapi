from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api
from ..controllers.filme_dao import FilmeDAO as dao

ns = api.namespace('filme','Filme')

@ns.route("/")
class FilmeService(Resource):

    def get(self):
        ''' Retorna todos os Filmes'''
        return make_response(jsonify({"filmes": dao().get_all()}), 200)