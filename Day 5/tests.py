import unittest

from queue import Queue
from queues import Queues


class Test_queue(unittest.TestCase):
    def test_queue_return(self):
        el = [1, 2, 3, 4, 5]
        q = Queue(el)
        out = q.return_queue
        self.assertEqual(out, el)

    def test_queue_push(self):
        q = Queue([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5, 6]
        q.push(6)
        out = q.return_queue
        self.assertEqual(out, expected)

    def test_queue_push_none_el(self):
        q = Queue([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        q.push(None)
        out = q.return_queue
        self.assertEqual(out, expected)

    def test_queue_pop(self):
        q = Queue([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4]
        q.pop()
        out = q.return_queue
        self.assertEqual(out, expected)

    def test_queue_pop_empty_list(self):
        q = Queue([])
        expected = []
        q.pop()
        out = q.return_queue
        self.assertEqual(out, expected)
    def test_queue_pop_compare_elements(self):
        q = Queue([1, 2, 3, 4, 5])
        expected = 5
        out = q.pop()
        self.assertEqual(out, expected)

    def test_queue_top(self):
        q = Queue([1, 2, 3, 4, 5])
        expected = 5
        out = q.check_top()
        self.assertEqual(out, expected)

    def test_is_empty_false(self):
        q = Queue([1, 2, 3, 4, 5])
        expected = False
        out = q.is_empty()
        self.assertEqual(out, expected)

    def test_is_empty_true(self):
        q = Queue([])
        expected = True
        out = q.is_empty()
        self.assertEqual(out, expected)

    def test_push_multiple(self):
        q = Queue([1, 2, 3])
        expected = [1, 2, 3, 4, 5]
        q.push_multiple_el([4,5])
        out = q.return_queue
        self.assertEqual(out, expected)

    def test_pop_multiple_compare_queues(self):
        q = Queue([1, 2, 3, 4, 5])
        expected = [1, 2, 3]
        q.pop_multiple_elements(2)
        out = q.return_queue
        self.assertEqual(out, expected)

    def test_pop_multiple_compare_return(self):
        q = Queue([1, 2, 3, 4, 5])
        expected = [4, 5]
        out = q.pop_multiple_elements(2)
        self.assertEqual(out, expected)


class Test_queues(unittest.TestCase):
    def test_create_queues(self):
        elements = [[1, 2, 3], [1, 2], [2, 3, 4]]
        out = Queues(elements).return_queues
        expected = {n: Queue(el).return_queue for n, el in enumerate(elements, 1)}
        self.assertEqual(out, expected)

    def test_execute_move_instruction(self):
        instruction = "move 2 from 1 to 2"
        queues_elements = [["A", "B", "C"], ["Z"]]
        queues = Queues(queues_elements)
        queues.execute_move_instruction(instruction)
        expected = {
            1: Queue(["A"]).return_queue,
            2: Queue(["Z", "C", "B"]).return_queue,
        }
        out = queues.return_queues
        self.assertEqual(expected, out)

    def test_read_values_from_string_template(self):
        string = "move 2 from 1 to 2"
        template = "move (?P<number>.*) from (?P<q1>.*) to (?P<q2>.*)"
        out = Queues.read_values_from_string_template(string, template)
        expected = {"number": "2", "q1": "1", "q2": "2"}
        self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()
