from typing import List

from queue import Queue
def create_queues(queues_elements: List[list]) -> dict:
    return {n: Queue(el) for n, el in enumerate(queues_elements, 1)}


