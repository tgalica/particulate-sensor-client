from airbornedata import AirborneData
from config import config
import pyrebase
# import jsonpickle

class Transmitter:
    def __init__(self):
        self.conf = config

    def transmit(self, airborne_data):
        print('calling transmit')
        firebase = pyrebase.initialize_app(config)

        db = firebase.database()

        # airborn_json = jsonpickle.encode(airborne_data)
        print(airborne_data)
        # print(airborne_json)
        # print(data)
        # db.child("airborne-data").push(airborne_json)
        
        # test = db.child("airborne-data").get()
        # print(test.val())