from typing import List
from queues import Queues
def read_queues(filename: str) ->Queues:
    q = []
    with open(filename, "r") as f:
        while line := f.readline().strip():
            q.append(line.split(" "))

    q_dropped_index = [el[1:] for el in q]
    return Queues(q_dropped_index)


def read_file_lines(filename: str) -> List[str]:
    ins = list()
    with open(filename, "r") as f:
        while line := f.readline().strip():
            ins.append(line)
    return ins

if __name__ == "__main__":
    q = read_queues("queues.txt")
    instructions = read_file_lines("instructions.txt")
    for i in instructions:
        q.execute_instruction(i)
    print("".join([el[-1] for el in q.return_queues.values()]))
