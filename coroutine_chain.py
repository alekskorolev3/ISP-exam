import asyncio
import requests

loop = asyncio.get_event_loop()


async def chain(url1, url2):
    print("Starting coroutines")
    await req1(url1)
    await req2(url2)
    print("Stop loading")


async def req1(url):
    print("Start req1")
    print(requests.get(url))


async def req2(url):
    print("Start req2")
    print(requests.get(url))


asyncio.run(chain("https://google.com", "https://yandex.ru"))
