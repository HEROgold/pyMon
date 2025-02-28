
from typing import override
from psutil import net_connections, net_if_addrs, net_if_stats, net_io_counters
from pymon.abc.stats import Stats
from pymon.abc.view_component import ViewComponent


class NetworkStats(Stats):
    def __init__(self) -> None:
        #See https://psutil.readthedocs.io/en/release-3.1.1/#network
        self._ios = net_io_counters(pernic=True)
        self._connections = net_connections
        self._addresses = net_if_addrs
        self._stats = net_if_stats

    @override
    def validate(self) -> bool:
        raise NotImplementedError

class NetworkMeter(ViewComponent):
    def __init__(self) -> None:
        super().__init__()
        self.stats = NetworkStats()

    def validate(self) -> None:
        self.stats.validate()
        raise NotImplementedError

    def render(self) -> None:
        raise NotImplementedError
