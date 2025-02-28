from abc import ABC, abstractmethod
from typing import Any

from pymon.abc.stats import Stats


class ViewComponent(ABC):
    width: int
    height: int
    x: int
    y: int
    content: Any
    stats: Stats

    @abstractmethod
    def validate(self) -> None:
        """Method to validate the component's content.
        
        It should always fit within its defined width and height."""
        pass

    @abstractmethod
    def render(self) -> None:
        """Render the component's content, within the given width and height."""
        pass
