from quru import NodeServer, raft
import asyncio

sender = NodeServer(role="sender", priority_queue=True, prefetch=5)
raft_core = raft.Core(sender)

task_counter = 0

@raft_core.register
async def periodically_dispatch(trace):
    while True:
        global task_counter
        flag = await sender.call("worker", task_counter)
        if flag == 1:
            print("Done task {}".format(task_counter))
        else:
            print("Failed task {}".format(task_counter))
        task_counter += 1
        await asyncio.sleep(5)


if __name__ == "__main__":
    sender.run()