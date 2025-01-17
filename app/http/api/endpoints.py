from flask_oidc import OpenIDConnect
from flask import Flask, json, g, request
from app.kudo.service import Service as Kudo
from app.kudo.schema import GitHubRepoSchema
from flask_cors import CORS

app = Flask(__name__)
app.config.update({
    'OIDC_CLIENT_SECRETS': './../../../../client_secrets.json',
    'OIDC_RESOURCE_SERVER_ONLY': True
})
oidc = OpenIDConnect(app)
CORS(app)

@app.route("/kudos", methods=["GET"])
@oidc.accept_token(True)
def index():
    return json_response(Kudo(g.oidc_token_info['sub']).find_all_kudos())



def json_response(payload, status=200):
    return (json.dump(payload), status, {'content-type': 'application/json'})