from django.test import TestCase
from .queue import UniqueQueue


class UniqueQueueTestCase(TestCase):
    def setUp(self):
        self.queue = UniqueQueue()

    def test_add_unique_value(self):
        self.queue.add(1)
        self.assertEqual(self.queue.length(), 1)
        self.assertEqual(self.queue.last(), 1)

    def test_add_duplicate_value(self):
        self.queue.add(1)
        self.queue.add(1)
        self.assertEqual(self.queue.length(), 1)

    def test_add_multiple_unique_values(self):
        values = [1, 2, 3, 4, 5]
        for value in values:
            self.queue.add(value)
        self.assertEqual(self.queue.length(), 5)

    def test_pop_value(self):
        self.queue.add(1)
        popped_value = self.queue.pop()
        self.assertEqual(popped_value, 1)
        self.assertEqual(self.queue.length(), 0)

    def test_pop_from_empty_queue(self):
        popped_value = self.queue.pop()
        self.assertIsNone(popped_value)

    def test_length_of_queue(self):
        values = [1, 2, 3]
        for value in values:
            self.queue.add(value)
        self.assertEqual(self.queue.length(), 3)

    def test_last_value_in_queue(self):
        values = [1, 2, 3]
        for value in values:
            self.queue.add(value)
        self.assertEqual(self.queue.last(), 3)

    def test_add_and_pop_multiple_values(self):
        values = [1, 2, 3]
        for value in values:
            self.queue.add(value)
        for value in values:
            self.assertEqual(self.queue.pop(), value)
        self.assertEqual(self.queue.length(), 0)

    def test_last_value_after_pop(self):
        self.queue.add(1)
        self.queue.add(2)
        self.assertEqual(self.queue.pop(), 2)
        self.assertEqual(self.queue.last(), 1)

    def test_add_large_number_of_unique_values(self):
        values = list(range(1, 1001))
        for value in values:
            self.queue.add(value)
        self.assertEqual(self.queue.length(), 1000)
        self.assertEqual(self.queue.last(), 1000)
