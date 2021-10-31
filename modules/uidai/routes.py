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

@app.route('/new', methods=['GET'])
@cross_origin()
def neww():
    csv_data = pd.read_csv('new_data.csv')
    try :
        data = []
        resp = {}
        csv_data_org = csv_data.loc[: , ['building','street','landmark','locality','vtc','district','state']]
        csv_data_list = csv_data_org.values.tolist()
        for row in csv_data_list:
            vtc = str(row[4])
            district = str(row[5])
            if str(vtc) == str(district):
                n_vtc = None
            else:
                n_vtc = vtc         
            record_dict = {'building' : row[0], 'street' : row[1], 'landmark' : row[2], 'locality' : row[3], 'vtc' : n_vtc, 'district' : row[5], 'state' : row[6]}
            data.append(record_dict)
        resp['data'] = data
        return jsonify(resp)
    except :
        pass        


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