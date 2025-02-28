
from typing import override
from psutil import boot_time, users
from pymon.abc.stats import Stats
from pymon.abc.view_component import ViewComponent


class MiscellaneousStats(Stats):
    def __init__(self) -> None:
        #See https://psutil.readthedocs.io/en/release-3.1.1/#other-system-info
        self._users = users
        self._boot_time = boot_time

    @override
    def validate(self) -> bool:
        raise NotImplementedError

class MiscellaneousMeter(ViewComponent):
    def __init__(self) -> None:
        super().__init__()
        self.stats = MiscellaneousStats()

    def validate(self) -> None:
        self.stats.validate()
        raise NotImplementedError

    def render(self) -> None:
        raise NotImplementedError
