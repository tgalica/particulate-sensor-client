from airbornedata import AirborneData
from config import config
import pyrebase

import json
# import jsonpickle

class Transmitter:
    def __init__(self):
        self.conf = config

    def transmit(self, airborne_data):
        print('calling transmit')
        firebase = pyrebase.initialize_app(config)

        db = firebase.database()

        # airborn_json = jsonpickle.encode(airborne_data)
        payload = json.dumps([x.getObjectAsDictionary() for x in airborne_data])
        # print(json.dumps(payload))
        # print(airborne_json)
        # print(data)
        db.child("airborne-data").push(payload)
        
        test = db.child("airborne-data").get()
        print(test.val())