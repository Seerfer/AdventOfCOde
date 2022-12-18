class Queue:
    def __init__(self, starting_elements: list = []):
        self.__queue = starting_elements

    def push(self, element) -> None:
        if element:
            self.__queue.append(element)

    def push_multiple_el(self, elements: list) -> None:
        if elements:
            for el in elements:
                self.push(el)

    def pop_multiple_elements(self, el_number):
        popped = list()
        if el_number:
            for _ in range(el_number):
                popped.append(self.pop())
        return popped[::-1]

    def is_empty(self) -> bool:
        return bool(not self.__queue)

    def pop(self):
        if self.__queue:
            return self.__queue.pop()

    def check_top(self):
        return self.__queue[-1]

    @property
    def return_queue(self):
        return self.__queue

    def __eq__(self, other) -> bool:
        if not isinstance(other, Queue):
            return NotImplemented
        return self.__queue == other.__queue
