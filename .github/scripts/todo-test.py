"""AI-assisted tests based on the UTS 43030 Lecture 4 practical."""

import io
import sys
import unittest

from todo import Task, TaskPool


class TestTask(unittest.TestCase):
    def test_new_task(self):
        task = Task("Write a report")
        self.assertEqual(task.title, "Write a report")
        self.assertEqual(task.status, "ToDo")
        self.assertFalse(task.completed)

    def test_mark_completed(self):
        task = Task("Write a report")
        task.mark_completed()
        self.assertEqual(task.status, "Done")
        self.assertTrue(task.completed)


class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        self.assertEqual(self.pool.tasks, [])
        task = Task("Run tests")
        self.pool.add_task(task)
        self.assertEqual(self.pool.tasks, [task])

    def test_get_open_tasks(self):
        self.assertEqual(self.pool.get_open_tasks(), [])
        first = Task("Write code")
        second = Task("Review code")
        third = Task("Run tests")
        second.mark_completed()
        for task in (first, second, third):
            self.pool.add_task(task)
        self.assertEqual(self.pool.get_open_tasks(), [first, third])

    def test_get_done_tasks(self):
        self.assertEqual(self.pool.get_done_tasks(), [])
        first = Task("Write code")
        second = Task("Review code")
        third = Task("Run tests")
        first.mark_completed()
        third.mark_completed()
        for task in (first, second, third):
            self.pool.add_task(task)
        self.assertEqual(self.pool.get_done_tasks(), [first, third])


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    output = io.StringIO()
    result = unittest.TextTestRunner(stream=output, verbosity=2).run(suite)
    sys.stdout.write(output.getvalue())
    sys.exit(0 if result.wasSuccessful() else 1)
