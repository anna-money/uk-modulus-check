import abc


class BaseTable(abc.ABC):
    @abc.abstractmethod
    def reload(self, lines: list[str]) -> None:
        ...
