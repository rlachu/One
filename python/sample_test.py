import unittest
from collections import namedtuple
from typing import Optional, TypeVar

from test_project import TestProject

T = TypeVar("T")


class TestCase(unittest.TestCase):

    # Tests:

    def test_success(self) -> None:
        testProject = TestProject()
        self.assertEqual('foo'.upper(), testProject.getCorrectUpperCase('foo'))

    def test_failure(self) -> None:
        testProject = TestProject()
        self.assertEqual('foo'.upper(), testProject.getWrongUpperCase('foo'))


if __name__ == "__main__":
    unittest.main()
