# import jsonpickle
import json
import datetime

class AirborneData:

    def __init__(self, sensor_id, sensor_name):
        self.sensor_name = sensor_name
        self.sensor_id = sensor_id
        self.data_collection_time = datetime.datetime.now()
        self.pm10_standard = 0
        self.pm25_standard = 0 
        self.pm100_standard= 0
        self.pm10_env = 0
        self.pm25_env = 0
        self.pm100_env = 0
        self.particles_03um = 0
        self.particles_05um = 0
        self.particles_10um = 0
        self.particles_25um = 0
        self.particles_50um = 0
        self.particles_100um = 0

    def getObjectAsDictionary(self):
        d = dict(
            sensor_id = self.sensor_id,
            sensor_name = self.sensor_name,
            data_collection_time = "ISODATE('" + self.data_collection_time.isoformat().__str__() + "')",
            pm10_standard = self.pm10_standard,
            pm25_standard = self.pm25_standard,
            pm100_standard = self.pm100_standard,
            pm10_env = self.pm10_env,
            pm25_env = self.pm25_env,
            pm100_env = self.pm100_env,
            particles_03um = self.particles_03um,
            particles_05um = self.particles_05um,
            particles_10um = self.particles_10um,
            particles_25um = self.particles_25um,
            particles_50um = self.particles_50um,
            particles_100um = self.particles_100um
        )
        return d
