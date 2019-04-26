import board
import busio
from digitalio import DigitalInOut, Direction
import serial

from airbornedata import AirborneData
from transmitter import Transmitter

try:
    import struct
except ImportError:
    import ustruct as struct

# Data collection variables
sensor_name = "Construction Hallway"
sensor_id = 2
transmitter = Transmitter()
airborne_data_list = []
########################

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Connect the Sensor's TX pin to the board's RX pin
#uart = busio.UART(board.TXD, board.RXD, baudrate=9600)
uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=3000)

buffer = []
print('entering loop')

i = 0

while i < 90:
    i = i + 1
    airborne = AirborneData(sensor_id, sensor_name)
    data = uart.read(32)  # read up to 32 bytes
    data = list(data)
    # print("read: ", data)          # this is a bytearray type

    buffer += data

    while buffer and buffer[0] != 0x42:
        buffer.pop(0)

    if len(buffer) > 200:
        buffer = []  # avoid an overrun if all bad data
    if len(buffer) < 32:
        continue

    if buffer[1] != 0x4d:
        buffer.pop(0)
        continue

    frame_len = struct.unpack(">H", bytes(buffer[2:4]))[0]
    if frame_len != 28:
        buffer = []
        continue

    #print(buffer)
    #print(buffer[4:])
    #frame = struct.unpack(">HHHHHHHHHHHHHH", bytes(buffer[4:]))
    frame = struct.unpack(">HHHHHHHHHHHHHH", bytes(buffer[4:]))

    pm10_standard, pm25_standard, pm100_standard, pm10_env, \
        pm25_env, pm100_env, particles_03um, particles_05um, particles_10um, \
        particles_25um, particles_50um, particles_100um, skip, checksum = frame

    check = sum(buffer[0:30])

    if check != checksum:
        buffer = []
        continue

    # Concentration Units (standard)
    airborne.pm10_standard = pm10_standard
    airborne.pm25_standard = pm25_standard
    airborne.pm100_standard = pm100_standard

    # Concentration Units (environmental)
    airborne.pm10_env = pm10_env
    airborne.pm100_env = pm100_env
    airborne.pm100_env = pm100_env

    # Particles
    airborne.particles_03um = particles_03um
    airborne.particles_05um = particles_05um
    airborne.particles_10um = particles_10um
    airborne.particles_25um = particles_25um
    airborne.particles_50um = particles_50um
    airborne.particles_100um = particles_100um
    
    airborne_data_list.append(airborne)

    # print(airborne)
    # print("Concentration Units (standard)")
    # print("---------------------------------------")
    # print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" %
    #       (pm10_standard, pm25_standard, pm100_standard))
    # print("Concentration Units (environmental)")
    # print("---------------------------------------")
    # print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" % (pm10_env, pm25_env, pm100_env))
    # print("---------------------------------------")
    # print("Particles > 0.3um / 0.1L air:", particles_03um)
    # print("Particles > 0.5um / 0.1L air:", particles_05um)
    # print("Particles > 1.0um / 0.1L air:", particles_10um)
    # print("Particles > 2.5um / 0.1L air:", particles_25um)
    # print("Particles > 5.0um / 0.1L air:", particles_50um)
    # print("Particles > 10 um / 0.1L air:", particles_100um)
    # print("---------------------------------------")

    buffer = buffer[32:]
    # print("Buffer ", buffer)

    if airborne_data_list.__len__() == 30:
        transmitter.transmit(airborne_data_list)
