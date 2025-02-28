from pymon.base.cpu import CPUMeter
from pymon.core.view import View


def main() -> None:
    view = View()
    view.add_component(CPUMeter())


if __name__ == "__main__":
    main()
