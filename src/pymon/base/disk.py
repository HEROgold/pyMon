
from functools import partial
from typing import override
from psutil import disk_io_counters, disk_partitions, disk_usage
from psutil._common import sdiskusage
from pymon.abc.stats import Stats
from pymon.abc.view_component import ViewComponent


class DiskStats(Stats):
    def __init__(self) -> None:
        #See https://psutil.readthedocs.io/en/release-3.1.1/#disks
        self._partitions = partial(disk_partitions, all=True)
        self._ios = partial(disk_io_counters, perdisk=True)

    def get_usages(self) -> list[sdiskusage]:
        return [
            disk_usage(disk)
            for disk in
            [partition.mountpoint for partition in self._partitions()]
        ]

    @override
    def validate(self) -> bool:
        raise NotImplementedError

class DiskMeter(ViewComponent):
    def __init__(self) -> None:
        super().__init__()
        self.stats = DiskStats()

    def validate(self) -> None:
        self.stats.validate()
        raise NotImplementedError

    def render(self) -> None:
        raise NotImplementedError
