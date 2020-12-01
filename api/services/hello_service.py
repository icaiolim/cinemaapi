from flask import jsonify, make_response, request
from flask_restx import Resource
from .. import api

ns = api.namespace('helloservice','Hello Service: recurso de teste da API')

@ns.route("/")
class HelloService(Resource):

    def __init__(self,api=None,*args,**kwargs):
        super(HelloService,self).__init__(api,args,kwargs)

    def get(self):
        ''' Retornar dados '''
        return make_response(
            jsonify(
                {
                    'mensagem': 'Hello World!'
                }
            ), 200
        )

    @api.doc(params={'dados': 'Informe os dados que serão adicionados'})
    def post(self):
        ''' Adicionar dados '''
        #exibir dados recebidos
        if self.api.payload is None:
            return make_response(
                jsonify({'erro': 'conteudo invalido'}), 406
            )
        print(self.api.payload)
        return make_response(
            jsonify({
                'mensagem': 'Dados inseridos com sucesso'
            })
        )


@ns.route("/<id>")
class HelloServiceItem(Resource):

    def delete(self, id):
        ''' Apagar dados a partir do ID'''
        print("Id: {}".format(id))
        return make_response(
            jsonify({
                'mensagem': 'Id {} apagado com sucesso'.format(id)
            })
        ) 

