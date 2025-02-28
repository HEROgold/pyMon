from functools import partial
from os import cpu_count
from typing import override
from pymon.abc.stats import Stats
from pymon.abc.view_component import ViewComponent
from psutil import cpu_percent, cpu_times


class CPUStats(Stats):
    def __init__(self) -> None:
        #See https://psutil.readthedocs.io/en/release-3.1.1/#cpu
        self._count = cpu_count
        self._times = partial(cpu_times, percpu=True)
        self._percent = partial(cpu_percent, interval=None, percpu=True)

    @override
    def validate(self) -> bool:
        count = self._count()
        if count is None:
            msg = "Could not determine the number of CPUs. Defaulting to 0 CPU."
            self.logger.warning(msg)
            count = 0
        return count >= 0


class CPUMeter(ViewComponent):
    def __init__(self) -> None:
        super().__init__()
        self.stats = CPUStats()

    def validate(self) -> None:
        self.stats.validate()
        raise NotImplementedError

    def render(self) -> None:
        raise NotImplementedError
