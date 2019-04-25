# import board
# import busio
# from digitalio import DigitalInOut, Direction
from airborndata import AirbornData
from transmitter import Transmitter

try:
    import struct
except ImportError:
    import ustruct as struct

# led = DigitalInOut(board.D13)
# led.direction = Direction.OUTPUT

# Connect the Sensor's TX pin to the board's RX pin
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

# buffer = []
i = 0
transmitter = Transmitter()
while i < 1:
    i = i + 1
    # data = uart.read(32)  # read up to 32 bytes
    # data = list(data)
    # print("read: ", data)          # this is a bytearray type

    # buffer += data

    # while buffer and buffer[0] != 0x42:
    #     buffer.pop(0)

    # if len(buffer) > 200:
    #     buffer = []  # avoid an overrun if all bad data
    # if len(buffer) < 32:
    #     continue

    # if buffer[1] != 0x4d:
    #     buffer.pop(0)
    #     continue

    # frame_len = struct.unpack(">H", bytes(buffer[2:4]))[0]
    # if frame_len != 28:
    #     buffer = []
    #     continue

    # frame = struct.unpack(">HHHHHHHHHHHHHH", bytes(buffer[4:]))
    airborn = AirbornData()
    # pm10_standard = 1
    # pm25_standard = 1 
    # pm100_standard= 1
    # pm10_env = 1
    # pm25_env = 1
    # pm100_env = 1
    # particles_03um = 1
    # particles_05um = 1
    # particles_10um = 1
    # particles_25um = 1
    # particles_50um = 1
    # particles_100um =1 
    # skip, checksum = frame

    # check = sum(buffer[0:30])

    # if check != checksum:
    #     buffer = []
    #     continue
    # print(dir(airborn))
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" %
          (airborn.pm10_standard, airborn.pm25_standard, airborn.pm100_standard))
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print("PM 1.0: %d\tPM2.5: %d\tPM10: %d" % (airborn.pm10_env, airborn.pm25_env, airborn.pm100_env))
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", airborn.particles_03um)
    print("Particles > 0.5um / 0.1L air:", airborn.particles_05um)
    print("Particles > 1.0um / 0.1L air:", airborn.particles_10um)
    print("Particles > 2.5um / 0.1L air:", airborn.particles_25um)
    print("Particles > 5.0um / 0.1L air:", airborn.particles_50um)
    print("Particles > 10 um / 0.1L air:", airborn.particles_100um)
    print("---------------------------------------")
    
    transmitter.transmit(airborn)

    # buffer = buffer[32:]
    # print("Buffer ", buffer)
