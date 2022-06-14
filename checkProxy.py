from grab import Grab, GrabError
import asyncio
import re
import requests

returnList = []


async def run_tasks(tasks):
    await asyncio.gather(*tasks)


async def checkProxy(proxy):
    global returnList
    g = Grab()
    g.setup(proxy=proxy, proxy_type='http', connect_timeout=2, timeout=2)
    try:
        g.go('https://www.instagram.com/')
        returnList.append(proxy)
        print(proxy + " success")
    except GrabError:
        pass
    return True


urls = [
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt',
]

proxies = ""

for url in urls:
    proxies += requests.get(url).text + " "

proxies = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b:\d{2,5}', proxies)
proxies = list(dict.fromkeys(proxies))
tasks = []
for proxy in proxies:
    tasks.append(checkProxy(proxy))
asyncio.get_event_loop().run_until_complete(run_tasks(tasks))
print(returnList)
