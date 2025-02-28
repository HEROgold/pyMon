from os import get_terminal_size
from pymon.abc.view_component import ViewComponent
from pymon.enum.border import BorderStyle


class View:
    width: int = get_terminal_size().columns
    height: int = get_terminal_size().lines
    border: BorderStyle = BorderStyle.NONE
    _components: list[ViewComponent]

    def validate(self) -> None:
        """Validate the view and it's components.
        
        Checks if each component is valid.
        And checks if each component may fit within the view's."""
        for component in self._components:
            component.validate()
            # TODO: Implement check if component fits within view's width and height

    def render(self) -> None:
        """Render the view and it's components."""
        for component in self._components:
            component.render()

    def add_component(self, component: ViewComponent) -> None:
        """Add a component to the view."""
        self._components.append(component)

    def remove_component(self, component: ViewComponent) -> None:
        """Remove a component from the view."""
        self._components.remove(component)
