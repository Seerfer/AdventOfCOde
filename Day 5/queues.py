import re
from typing import List

from queue import Queue


class Queues:
    def __init__(self, queues_elements: List[list]):
        self.__queues = {n: Queue(el) for n, el in enumerate(queues_elements, 1)}

    def execute_move_instruction(self, instruction: str, multiple_el: bool = False) -> None:
        template = "move (?P<number>.*) from (?P<q1>.*) to (?P<q2>.*)"
        parsed = self.read_values_from_string_template(instruction, template)
        if multiple_el:
            popped = self.__queues[int(parsed.get("q1"))].pop_multiple_elements(int(parsed.get("number")))
            self.__queues[int(parsed.get("q2"))].push_multiple_el(popped)
        else:
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
