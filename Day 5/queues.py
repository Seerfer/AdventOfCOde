from queue import Queue

class Queues:
    def __init__(self, queues_elements: dict):
        self.__queues = {n: Queue(el) for n, el in enumerate(queues_elements, 1)}

    @property
    def return_queues(self):
        return self.__queues