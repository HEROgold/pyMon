from typing import override
from psutil import swap_memory, virtual_memory
from pymon.abc.stats import Stats
from pymon.abc.view_component import ViewComponent


class MemoryStats(Stats):
    def __init__(self) -> None:
        #See https://psutil.readthedocs.io/en/release-3.1.1/#memory
        self._virtual = virtual_memory
        self._swap = swap_memory

    @override
    def validate(self) -> bool:
        raise NotImplementedError

class MemoryMeter(ViewComponent):
    def __init__(self) -> None:
        super().__init__()
        self.stats = MemoryStats()

    def validate(self) -> None:
        self.stats.validate()
        raise NotImplementedError

    def render(self) -> None:
        raise NotImplementedError
