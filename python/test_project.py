from collections import OrderedDict
from dataclasses import dataclass
from threading import RLock
from typing import Generic, Optional, Tuple, TypeVar


class TestProject:

    def __init__(self):
        self._lock = RLock()

    def getCorrectUpperCase(self, val: str) -> str:
        with self._lock:
            return val.upper()

    def getWrongUpperCase(self, val: str) -> str:
        with self._lock:
            return val.lower()
