import asyncio
import websockets

@asyncio.coroutine
def hello(websocket, path):
    name = yield from websocket.recv()
    print("< {}".format(name))
    greeting = "Hello!"
    yield from websocket.send(greeting)
    print("> {}".format(greeting))

start_server = websockets.serve(hello, 'localhost', 8765, origins = ["*", ''], extra_headers = [('Access-Control-Allow-Origin', '*')])

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
