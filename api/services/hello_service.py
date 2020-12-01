from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api

ns = api.namespace('helloservice','Hello Service: recurso de teste da API')

@ns.route("/")
class HelloService(Resource):

    def __init__(self,api=None,*args,**kwargs):
        super(HelloService,self).__init__(api,args,kwargs)


@ns.route("/<id>")
class HelloServiceItem(Resource):

    @api.doc(params={'data': 'Informe o dado que será alterado'})
    def put(self, id):
        ''' Atualizar dado a partir do ID'''
        if self.api.payload is None or self.api.payload.get('data') is None:
            return make_response(
                jsonify({'erro': 'conteudo invalido'}), 406
            )

        data = self.api.payload.get('data')
        return make_response(
            jsonify({
                'id': int(id),
                'data': '{}'.format(data)
            })
        )

    def delete(self, id):
        ''' Apagar dados a partir do ID'''
        print("Id: {}".format(id))
        return make_response(
            jsonify({
                'id': int(id),
                'mensagem': 'Id {} apagado com sucesso'.format(id)
            })
        ) 

