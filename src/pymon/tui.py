from pymon.core.view import View


class TuiManager:
    def __init__(self) -> None:
        self._screens: list[View] = []

    def add_screen(self, screen: View) -> None:
        self._screens.append(screen)

    def remove_screen(self, screen: View) -> None:
        self._screens.remove(screen)

    def run(self) -> None:
        for screen in self._screens:
            screen.render()
