import asyncio
import random

loop = asyncio.get_event_loop()


async def worker():
    seconds = random.randint(1, 2)

    print("Worker 1 start")

    await asyncio.sleep(seconds)

    print("Worker 1 exited")


async def service():
    seconds = random.randint(1, 2)

    print("Worker 2 start")

    await asyncio.sleep(seconds)

    print("Worker 2 exited")

tasks = [loop.create_task(worker()), loop.create_task(service())]
wait_object = asyncio.wait(tasks)
loop.run_until_complete(wait_object)
loop.close()