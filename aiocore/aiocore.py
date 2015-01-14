import asyncio
import weakref


class Service:
    identifier = None
    _registry = weakref.WeakValueDictionary()

    def __init__(self):
        if self.identifier is None:
            raise ValueError("No identifier defined.")
        Service._registry[self.identifier] = self

    @classmethod
    def resolve(cls, name):
        return cls._registry[name]

    @asyncio.coroutine
    def __call__(self):
        raise NotImplementedError("No such run")


class EventService(Service):
    def __init__(self):
        super(EventService, self).__init__()
        self._queue = asyncio.Queue()

    @asyncio.coroutine
    def handle(self, message):
        raise NotImplementedError("Not implemented")

    @asyncio.coroutine
    def send(self, message):
        return (yield from self._queue.put(message))

    @asyncio.coroutine
    def __call__(self):
        while True:
            message = (yield from self._queue.get())
            yield from self.handle(message)
