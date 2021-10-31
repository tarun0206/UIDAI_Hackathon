from __future__ import division
from logging import error
from os import stat
from flask import blueprints, request, jsonify, make_response, Blueprint
from flask_cors import CORS, cross_origin
from modules import app
import pandas as pd
import googletrans
from googletrans import Translator
import json

uidai_module = Blueprint('uidai', __name__)
CORS(app)

@app.route('/newapi', methods=['GET'])
@cross_origin()
def nnewapi():
    r = request.json
    buildingg = request.json['building']
    street = r['street']
    locality = r['locality']
    vtc = r['vtc']
    district = r['district']
    landmark = r['landmark']
    state = r['state']
    if locality == vtc:
        locality = ""
    if vtc == district:
        vtc = ""
    if district == state:
        district = ""
    record = {
        'building' : buildingg,
        'street' : street,
        'locality' : locality,
        'vtc' : vtc,
        'district' : district,
        'landmark' : landmark,
        'state' : state

    }
    return(jsonify(record)) 