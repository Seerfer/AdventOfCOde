import unittest

from Queue import Queue
from main import create_queues

class Test_stack(unittest.TestCase):

    def test_queue_return(self):
        el = [1, 2, 3, 4, 5]
        q = Queue(el)
        out = q.return_queue
        self.assertEqual(out, el)

    def test_queue_push(self):
        q = Queue([1,2,3,4,5])
        expected = [1,2,3,4,5,6]
        q.push(6)
        out = q.return_queue
        self.assertEqual(out, expected)

    def test_queue_pop_compare_queue(self):
        q = Queue([1,2,3,4,5])
        expected = [1,2,3,4]
        q.pop()
        out = q.return_queue
        self.assertEqual(out, expected)

    def test_queue_pop_compare_elements(self):
        q = Queue([1,2,3,4,5])
        expected = 5
        out = q.pop()
        self.assertEqual(out, expected)

    def test_queue_top(self):
        q = Queue([1,2,3,4,5])
        expected = 5
        out = q.check_top()
        self.assertEqual(out, expected)

    def test_is_empty_false(self):
        q = Queue([1,2,3,4,5])
        expected = False
        out = q.is_empty()
        self.assertEqual(out, expected)

    def test_is_empty_true(self):
        q = Queue([])
        expected = True
        out = q.is_empty()
        self.assertEqual(out, expected)


class Test_functions(unittest.TestCase):

    def test_create_queues(self):
        elements = [[1,2,3], [1,2], [2,3,4]]
        out = create_queues(elements)
        expected = {n: Queue(el) for n, el in enumerate(elements, 1)}
        self.assertEqual(out, expected)

if __name__ == "__main__":
    unittest.main()