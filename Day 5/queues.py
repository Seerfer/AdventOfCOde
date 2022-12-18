import re
from typing import List

from queue import Queue

class Queues:
    def __init__(self, queues_elements: List[list]):
        self.__queues = {n: Queue(el) for n, el in enumerate(queues_elements, 1)}

    def execute_instruction(self, instruction: str) -> None:
        pass

    @staticmethod
    def read_values_from_string_template(string:str, template:str) -> dict:
        m = re.match(rf'{template}', string)
        return m.groupdict()

    @property
    def return_queues(self):
        return self.__queues