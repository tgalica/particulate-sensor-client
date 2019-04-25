import requests


# pm10_standard, pm25_standard, pm100_standard, pm10_env,
# pm25_env, pm100_env, particles_03um, particles_05um, particles_10um,
# particles_25um, particles_50um, particles_100um, skip, checksum = frame

resp = requests.get('http://www.google.com')
print(resp)