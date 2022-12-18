
class Queue:

    def __init__(self, starting_elements: list = []):
        self.__queue = starting_elements

    def push(self, element) -> None:
        self.__queue.append(element)

    def is_empty(self) -> bool:
        return bool(not self.__queue)

    def pop(self):
        return self.__queue.pop()

    def check_top(self):
        return self.__queue[-1]

    @property
    def return_queue(self):
        return self.__queue
