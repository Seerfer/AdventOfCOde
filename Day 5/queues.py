import re
from typing import List

from queue import Queue


class Queues:
    def __init__(self, queues_elements: List[list]):
        self.__queues = {n: Queue(el) for n, el in enumerate(queues_elements, 1)}

    def execute_instruction(self, instruction: str) -> None:
        template = "move (?P<number>.*) from (?P<q1>.*) to (?P<q2>.*)"
        parsed = self.read_values_from_string_template(instruction, template)
        for _ in range(int(parsed["number"])):
            el = self.__queues[int(parsed.get("q1"))].pop()
            self.__queues[int(parsed.get("q2"))].push(el)

    @staticmethod
    def read_values_from_string_template(string: str, template: str) -> dict:
        m = re.match(template, string)
        return m.groupdict()

    @property
    def return_queues(self):
        return {n: q.return_queue for n, q in self.__queues.items()}
