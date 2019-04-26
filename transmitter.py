from airbornedata import AirborneData
from config import config
import pyrebase

import json

class Transmitter:
    def __init__(self):
        self.conf = config

    def transmit(self, airborne_data):
        print('calling transmit')
        firebase = pyrebase.initialize_app(config)

        db = firebase.database()

        payload = json.dumps([x.getObjectAsDictionary() for x in airborne_data])
        print(payload)
        db.child("airborne-data").push(payload)
        
        # test = db.child("airborne-data").get()
        # print(test.val())