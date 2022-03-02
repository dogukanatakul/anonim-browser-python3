import random
import json


def getDevice():
    devices = []
    file = open('user-agents.txt', 'r')
    for line in file:
        devices.append(line)
    file.close()
    return ''.join(random.choice(devices))


def getLocation():
    locations = []
    file = open('locations.txt', 'r')
    for line in file:
        locations.append(line)
    file.close()
    explode = random.choice(locations).split("/")
    return explode


def getSetting(column):
    file = open('settings.json', 'r')
    file = file.read()
    data = json.loads(file)
    return data[column]
