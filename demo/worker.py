from quru import NodeServer
import asyncio

worker = NodeServer(role="worker", priority_queue=True, prefetch=5)

@worker.register
async def do_the_task(data):
    print("Receiving task: {}.".format(data))
    print("Doing...")
    await asyncio.sleep(1)
    if data % 2 == 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    worker.run()