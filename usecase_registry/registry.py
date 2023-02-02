"""Registry containers for kinda workflow use case implementation."""

from typing import Generic, TypeVar

T = TypeVar("T")


class UseCaseRegistry(Generic[T]):
    """Use to capture elements from use case workflow execution."""

    def __init__(self, max_length: int) -> None:
        """
        Use case registry.

        Used to capture useful objects like write operations to be executed
        as a transaction, use case workflow execution result, or triggered
        and handled expections.
        """
        self.max_length = max_length

        self._already_checked = False
        self._storage: list[T] = []

    def is_empty(self) -> bool:
        """Check if registry storage is empty."""
        return len(self._storage) == 0

    def add_value(self, v: T) -> None:
        """Add value to the registry storage."""
        if not isinstance(v, self.__orig_class__.__args__[0]):  # type: ignore[attr-defined] # noqa: E501
            raise ValueError("The registry only accepts values of configured datatype.")

        if len(self._storage) >= self.max_length:
            raise RuntimeError("Storage exceeded max length configured.")

        self._storage.append(v)

    def get_state(self) -> list[T]:
        """Return, only once, the state of the registry."""
        if self._already_checked:
            raise RuntimeError("Storage has already been checked.")

        self._already_checked = True
        return self._storage