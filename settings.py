import random
import json


def getDevice():
    devices = []
    file = open('user-agents.txt', 'r')
    for line in file:
        devices.append(line)
    file.close()
    return ''.join(random.choice(devices).replace("\n", ""))


def getProxies():
    proxies = []
    file = open('proxies.txt', 'r')
    for line in file:
        proxies.append(line)
    file.close()
    proxy = random.choice(proxies).split(":")
    if len(proxy) > 2:
        return {
            'ip': str(proxy[0]),
            'port': int(proxy[1]),
            'user': proxy[2],
            'pass': proxy[3].replace("\n", ""),
        }
    else:
        return {
            'ip': str(proxy[0]),
            'port': int(proxy[1].replace("\n", "")),
            'user': None,
            'pass': None,
        }


def getLocation():
    locations = []
    file = open('locations.txt', 'r')
    for line in file:
        locations.append(line)
    file.close()
    explode = random.choice(locations).replace("\n", "").split("/")
    return explode


def getSetting(column):
    file = open('settings.json', 'r')
    file = file.read()
    data = json.loads(file)
    return data[column]
