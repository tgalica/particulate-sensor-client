from airborndata import AirbornData
from config import config
import pyrebase
import jsonpickle

class Transmitter:
    def __init__(self):
        self.conf = config

    def transmit(self, airborn_data):
        print(config)
        print(airborn_data)
        firebase = pyrebase.initialize_app(config)

        db = firebase.database()

        airborn_json = jsonpickle.encode(airborn_data)
        # print(data)
        db.child("airborn-data").push(airborn_json)
        
        test = db.child("airborn-data").get()
        print(test.val())