from flask import Flask, request, jsonify
from flask.ext.restful import Resource, Api
from models import Nacional

app = Flask(__name__)
api = Api(app)


class CNE(Resource):
    def get(self, cedula):
        registro = Nacional.query.filter_by(cedula=cedula).first()
        if registro is not None:
            return registro.as_dict()
        else:
            return {}



api.add_resource(CNE, '/<string:cedula>')

if __name__ == '__main__':
    app.run(debug=True)
